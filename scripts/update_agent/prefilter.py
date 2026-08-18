"""Deterministic, source-aware Phase-1 prefilter (recall-conscious noise removal).

Runs BEFORE cross-source merge and the Claude relevance scorer. It removes obvious noise using
only lightweight metadata already allowed in Phase 1 — it is NOT the final inclusion decision.

Design: require *combined* evidence, not any single keyword.
  arXiv / OpenReview : an evaluation/benchmark signal AND an agent-or-science signal, OR a
                       strong compound phrase ("agent benchmark", "scientific agent", ...).
  GitHub            : the same combined signal AND not matching a repo-noise pattern
                       (awesome-*, skill/prompt collections, templates, MCP servers, generic
                       frameworks/SDKs/tooling, tutorials/demos, personal apps).
"""
import re

# --- signal vocabularies (word-ish boundaries; case-insensitive) ---
EVAL = re.compile(r"\b(benchmark(s|ing)?|eval(s|uation|uations|uating|uate)?|testbed|"
                  r"leaderboard|arena|gym(nasium)?|test\s?suite|diagnostic|probe|"
                  r"assessment|evaluation environment)\b", re.I)
AGENT = re.compile(r"\b(agent|agents|agentic|multi-?agent|tool[-\s]?use|function[-\s]?calling|"
                   r"trajector(y|ies)|autonomous|embodied|react|language[-\s]model[-\s]agent|"
                   r"llm[-\s]?agent)\b", re.I)
SCI = re.compile(r"\b(scientif\w+|science|research|experiment\w*|laborator\w+|\blab\b|"
                 r"simulat\w+|discovery|hypothes\w+|physic\w*|chemi\w+|biolog\w+|material\w*|"
                 r"astronom\w+|mathemat\w+|engineering|clinical|medical|genomic\w*|"
                 r"bioinformatic\w*|scientific computing|molecular|quantum|pde)\b", re.I)
# An LLM/foundation-model signal. This repo is an LLM/agent-evaluation catalog, so for a PAPER the
# evaluation signal must pair with an agent OR LLM angle — a science paper that merely has a
# benchmark/eval word but no agent/LLM angle (the old EVAL+SCI floodgate) is out of scope.
LLM = re.compile(r"\b(llm|llms|large language model(s)?|language model(s)?|foundation model(s)?|"
                 r"gpt[-\s]?\d|multimodal model(s)?|vision[-\s]language(?:[-\s]action)?)\b", re.I)
# A concrete benchmark/environment noun — required for a standalone GitHub repo (a repo merely
# describing itself as a "research agent" is not evidence of a catalogable evaluation work).
EVAL_STRONG = re.compile(r"\b(benchmark(s|ing)?|testbed|leaderboard|arena|gym(nasium)?|"
                         r"test\s?suite|benchmark\s?suite|eval(uation)?\s+(suite|environment|harness))\b", re.I)
STRONG = re.compile(
    r"(agent(ic)?\s+benchmark|benchmark\w*\s+(for|of)\s+[\w\s-]{0,30}agent|"
    r"evaluat\w+\s+[\w\s-]{0,30}agent|agent\s+evaluation|scientific\s+agent|research\s+agent|"
    r"ai\s+scientist|autonomous\s+research|self-?driving\s+lab|trajectory\s+evaluation|"
    r"process[-\s](level|reward)|evaluation\s+environment|benchmark\s+suite|"
    r"long-?horizon\s+agent)", re.I)

# GitHub repo-noise patterns (matched on name / topics primarily, description secondarily)
GH_NOISE = re.compile(
    r"(awesome[-_]|[-_]awesome|(^|[-_])skills?([-_]|$)|skill[-_]?collection|"
    r"prompt[-_]?(collection|library|list|s\b)|template|boilerplate|starter|scaffold|"
    r"mcp[-_]?server|(^|[-_])sdk([-_]|$)|tutorial|example(s)?|demo|cookbook|playground|"
    r"wrapper|(^|[-_])client([-_]|$)|plugin|extension|portfolio|homepage|cheat[-_]?sheet|"
    r"roadmap|(^|[-_])course([-_]|$)|chatbot|chat[-_]?app)", re.I)


def _text_paper(rec):
    return "%s . %s" % (rec.get("title", ""), rec.get("abstract_or_description", ""))


def _combined(text):
    # PAPER gate (arXiv/OpenReview). A strong compound phrase (agent benchmark, scientific agent,
    # AI scientist, trajectory evaluation, evaluation environment, …) always passes. Otherwise an
    # evaluation signal must pair with EITHER an agent angle OR (a scientific angle AND an LLM angle).
    # This closes the old EVAL+SCI floodgate — a science paper with a benchmark word but no agent and
    # no LLM is out of scope — WITHOUT opening an EVAL+LLM floodgate for generic NLP/coding benchmarks
    # that have neither a scientific nor an agent angle. (Calibration audit: the bare EVAL+SCI path
    # admitted 131/432 arXiv records, largely generic-science/ML benchmarks.)
    return bool(STRONG.search(text)
                or (EVAL.search(text) and (AGENT.search(text) or (SCI.search(text) and LLM.search(text)))))


def judge(rec):
    """Return (keep: bool, reason: str)."""
    src = rec.get("source")
    # HuggingFace daily-papers records are papers with a title and an abstract, so they take the
    # same path as arXiv/OpenReview. This matters: the curated feed carries ~30 papers a day across
    # all of ML, and without the paper filter the whole feed would reach the relevance scorer and
    # crowd out the deep-review cap.
    if src in ("arxiv", "openreview", "huggingface"):
        if _combined(_text_paper(rec)):
            return True, "eval+agent/science signal"
        return False, "no evaluation+agent/science evidence"
    if src == "github":
        name = rec.get("id", "") or rec.get("title", "")
        topics = " ".join(rec.get("topics", []) or [])
        desc = rec.get("abstract_or_description", "")
        if GH_NOISE.search(name) or GH_NOISE.search(topics):
            return False, "github repo-noise pattern (name/topics)"
        text = "%s . %s . %s" % (name, desc, topics)
        # standalone repo must name an actual benchmark/environment AND be agent/science-related
        if not (EVAL_STRONG.search(text) and (AGENT.search(text) or SCI.search(text))):
            return False, "github not a benchmark/environment for agents/science"
        if GH_NOISE.search(desc):
            return False, "github repo-noise pattern (description)"
        return True, "github benchmark/environment for agents/science"
    return True, "unknown source kept"


def run(raw):
    """raw: list of records -> (kept, rejected). rejected items carry a 'prefilter_reason'."""
    kept, rejected = [], []
    for rec in raw:
        ok, reason = judge(rec)
        if ok:
            kept.append(rec)
        else:
            r = {"source": rec.get("source"), "id": rec.get("id"),
                 "title": rec.get("title"), "prefilter_reason": reason}
            rejected.append(r)
    return kept, rejected
