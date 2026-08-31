const ui = {
  en: {
    tabs: { home: "Home", topics: "Topics", domains: "Domains", activities: "Activities", monthly: "Monthly", works: "Works" },
    heroTitle: "Scientific Evaluation Environments",
    heroText: "A living knowledge base for scientific and engineering AI agent evaluation. See what each benchmark measures, what its results reveal, and what developers can improve next. Browse by topic, domain, activity, or month.",
    readmeLink: "Guide",
    monthlyLink: "Monthly",
    githubLink: "GitHub repository",
    homeWhyTitle: "What this repository is for",
    homeWhyText: "A benchmark score is useful only if it helps you decide what to change next. This repository collects work that makes evaluation more diagnostic, more legible, and more useful for building scientific and engineering agents.",
    homePoints: [
      ["Measure", "What is being tested, and what evidence does the score actually see?"],
      ["Diagnose", "If the agent fails, can you tell whether the problem is planning, execution, judging, or task design?"],
      ["Improve", "Can evaluation guide the next intervention on skills, harnesses, data, or post-training?"]
    ],
    axesKicker: "How to read the corpus",
    axesTitle: "Three ways into the same work card",
    overviewCards: [
      ["Topics", "Start here if your question is about an evaluation problem: planning, trajectories, judges, resource use, benchmark validity, or post-training."],
      ["Domains", "Start here if your question is about a field: physics, chemistry, biology, robotics, civil engineering, and more."],
      ["Activities", "Start here if your question is about what the agent actually does: literature review, simulation, experiment design, reproduction, or end-to-end research."]
    ],
    automationKicker: "Maintenance flow",
    automationTitle: "How the repository stays current",
    automationText: "The repository updates in two rhythms: every three days for new works, and every month for synthesis.",
    automationCards: [
      ["Every three days", "The update agent searches public sources, drafts work cards and index updates, and opens a pull request for review instead of publishing directly."],
      ["Every month", "The monthly report summarizes what entered the knowledge base and what those works changed together, with English and Chinese versions kept in sync."]
    ],
    homeMonthlyKicker: "Recent synthesis",
    homeMonthlyTitle: "Recent monthly reports",
    topicsKicker: "Evaluation questions",
    topicsTitle: "Topics",
    topicsText: "Topics group work by the evaluation problem it addresses.",
    domainsKicker: "Scientific and engineering fields",
    domainsTitle: "Domains",
    domainsText: "Domain pages answer where a benchmark or method is grounded.",
    activitiesKicker: "What the agent does",
    activitiesTitle: "Activities",
    activitiesText: "Activities group work by the actual scientific or research task under evaluation.",
    monthlyKicker: "Research stories over time",
    monthlyTitle: "Monthly reports",
    monthlyText: "Monthly reports summarize what entered the knowledge base and what that cluster of work changed in the field.",
    timelineTitle: "First-appearance timeline",
    timelineText: "Each bar counts works by earliest public appearance month.",
    worksKicker: "Card-level lookup",
    worksTitle: "Works",
    worksText: "Search by title or summary, then narrow by topic, domain, activity, or month.",
    readerEmpty: "Select any topic, domain, activity, monthly report, or work card to render it here as HTML.",
    footerText: "Generated from Markdown source files in the repository. If content disagrees, trust the Markdown.",
    stats: { works: "Work cards", topics: "Topics", domains: "Domains", activities: "Activities", monthlyReports: "Monthly reports" },
    filters: { search: "Search works", allTopics: "All topics", allDomains: "All domains", allActivities: "All activities", allMonths: "All months" },
    resultsTitle: "Works",
    resultsCount: (n) => `${n} works shown`,
    firstAppeared: "First appeared",
    source: "Source",
    topics: "Topics",
    domains: "Domains",
    activities: "Activities",
    links: "Links",
    monthlyWorks: (n) => `${n} works`,
    openPage: "Open here",
  },
  zh: {
    tabs: { home: "首页", topics: "Topics", domains: "Domains", activities: "Activities", monthly: "月报", works: "Works" },
    heroTitle: "Scientific Evaluation Environments",
    heroText: "这是一个持续更新的知识库，收集科学与工程 AI agent 的评估工作。它不只记录 benchmark 分数，还关心分数说明了什么、失败出在哪儿、下一步该改什么。你可以按 topic、domain、activity 或月份浏览。",
    readmeLink: "仓库导览",
    monthlyLink: "月报",
    githubLink: "GitHub 仓库",
    homeWhyTitle: "这个仓库到底是干啥的",
    homeWhyText: "一个 benchmark 分数真正有用，不是因为它告诉你成没成，而是因为它能帮你判断下一步该改哪儿。这个仓库收的，就是把 evaluation 变得更能诊断、更容易看懂、也更能指导改系统的工作。",
    homePoints: [
      ["Measure", "它到底在测什么？这个分数看到了哪些证据，没看到哪些证据？"],
      ["Diagnose", "agent 失败以后，你能不能分清是 planning、execution、judge，还是 task design 出了问题？"],
      ["Improve", "evaluation 能不能真正指导下一步去改 skill、harness、data 或 post-training？"]
    ],
    axesKicker: "怎么读这个仓库",
    axesTitle: "同一张 work card，有三种读法",
    overviewCards: [
      ["Topics", "如果你关心的是评估问题本身，比如 planning、trajectory、judge、resource use、benchmark validity、post-training，就从这里进。"],
      ["Domains", "如果你关心的是具体学科，比如 physics、chemistry、biology、robotics、civil engineering，就从这里进。"],
      ["Activities", "如果你关心的是 agent 实际在干嘛，比如文献综述、simulation、实验设计、复现、端到端研究，就从这里进。"]
    ],
    automationKicker: "维护流程",
    automationTitle: "这个仓库怎么保持更新",
    automationText: "仓库有两个节奏：每三天补新 work，每个月做一次综合月报。",
    automationCards: [
      ["每三天", "自动更新 agent 会去公开来源找新 work，起草 card 和索引更新，然后发 PR 给人审，不会直接往 main 里写。"],
      ["每个月", "月报负责把新进入知识库的一批工作串成研究故事，并保持英文与中文版本同步。"]
    ],
    homeMonthlyKicker: "最近的综合总结",
    homeMonthlyTitle: "最近月报",
    topicsKicker: "评估问题",
    topicsTitle: "Topics",
    topicsText: "Topic 是按它在解决哪个 evaluation 问题来组织的。",
    domainsKicker: "科学与工程领域",
    domainsTitle: "Domains",
    domainsText: "Domain 页回答的是：这个 benchmark 或方法到底落在哪个学科。",
    activitiesKicker: "agent 实际在做什么",
    activitiesTitle: "Activities",
    activitiesText: "Activity 是按被评估 agent 实际执行的研究任务来组织的。",
    monthlyKicker: "按时间看研究脉络",
    monthlyTitle: "月度报告",
    monthlyText: "月报讲的是进入知识库的一批 work 合在一起改变了什么，不只是按日期列清单。",
    timelineTitle: "首次公开时间线",
    timelineText: "每根柱子表示这个月最早公开的 work 数量。",
    worksKicker: "按卡片查",
    worksTitle: "Works",
    worksText: "先按标题或摘要搜，再按 topic、domain、activity、month 收窄。",
    readerEmpty: "点任意 topic、domain、activity、月报或 work card，就会在这里按 HTML 打开。",
    footerText: "本页由仓库 Markdown 自动生成。如果页面内容和 Markdown 冲突，以 Markdown 为准。",
    stats: { works: "工作卡片", topics: "Topics", domains: "Domains", activities: "Activities", monthlyReports: "月报" },
    filters: { search: "搜索 works", allTopics: "全部 topics", allDomains: "全部 domains", allActivities: "全部 activities", allMonths: "全部月份" },
    resultsTitle: "Works",
    resultsCount: (n) => `当前显示 ${n} 项 work`,
    firstAppeared: "首次公开",
    source: "来源",
    topics: "Topics",
    domains: "Domains",
    activities: "Activities",
    links: "链接",
    monthlyWorks: (n) => `${n} 项工作`,
    openPage: "在这里打开",
  }
};

let state = {
  lang: localStorage.getItem("scieval-explorer-language") || (navigator.language.toLowerCase().startsWith("zh") ? "zh" : "en"),
  data: null,
  activeTab: "home",
  filters: { search: "", topic: "", domain: "", activity: "", month: "" },
  reader: { url: "./documents/en/README.json", title: "Reader" }
};

const byId = (id) => document.getElementById(id);

function setText(id, text) {
  const node = byId(id);
  if (node) node.textContent = text;
}

function localizedDocumentUrl(url, lang = state.lang) {
  if (!url) return url;
  const target = new URL(url, window.location.href);
  if (target.origin !== window.location.origin || !/\/documents\/(?:en|zh)\/.+\.json$/.test(target.pathname)) return url;
  target.pathname = target.pathname.replace(/\/documents\/(?:en|zh)\//, `/documents/${lang}/`);
  return target.href;
}

function localizedItemName(item) {
  return state.lang === "zh" ? (item.zh_name || item.name) : item.name;
}

function localizedItemUrl(item) {
  return state.lang === "zh" ? (item.zh_url || localizedDocumentUrl(item.url, "zh")) : item.url;
}

function applyUiText() {
  const t = ui[state.lang];
  setText("hero-title", t.heroTitle);
  setText("hero-text", t.heroText);
  setText("readme-link", t.readmeLink);
  setText("monthly-link", t.monthlyLink);
  setText("github-link", t.githubLink);
  byId("readme-link").href = localizedDocumentUrl("./documents/en/README.json");
  byId("monthly-link").href = localizedDocumentUrl("./documents/en/monthly/README.json");
  setText("home-why-title", t.homeWhyTitle);
  setText("home-why-text", t.homeWhyText);
  setText("axes-kicker", t.axesKicker);
  setText("axes-title", t.axesTitle);
  setText("automation-kicker", t.automationKicker);
  setText("automation-title", t.automationTitle);
  setText("automation-text", t.automationText);
  setText("home-monthly-kicker", t.homeMonthlyKicker);
  setText("home-monthly-title", t.homeMonthlyTitle);
  setText("topics-kicker", t.topicsKicker);
  setText("topics-title", t.topicsTitle);
  setText("topics-text", t.topicsText);
  setText("domains-kicker", t.domainsKicker);
  setText("domains-title", t.domainsTitle);
  setText("domains-text", t.domainsText);
  setText("activities-kicker", t.activitiesKicker);
  setText("activities-title", t.activitiesTitle);
  setText("activities-text", t.activitiesText);
  setText("monthly-kicker", t.monthlyKicker);
  setText("monthly-title", t.monthlyTitle);
  setText("monthly-text", t.monthlyText);
  setText("timeline-title", t.timelineTitle);
  setText("timeline-text", t.timelineText);
  setText("works-kicker", t.worksKicker);
  setText("works-title", t.worksTitle);
  setText("works-text", t.worksText);
  setText("results-title", t.resultsTitle);
  setText("footer-text", t.footerText);
  Object.entries(t.tabs).forEach(([key, label]) => setText(`tab-${key}`, label));
  byId("search").placeholder = t.filters.search;
  byId("lang-toggle").textContent = state.lang === "en" ? "中文" : "English";
}

function renderHomeBlocks() {
  const t = ui[state.lang];
  byId("home-points").innerHTML = t.homePoints.map(([title, text]) => `
    <article class="key-point">
      <h3>${title}</h3>
      <p>${text}</p>
    </article>
  `).join("");
  byId("overview-cards").innerHTML = t.overviewCards.map(([title, text]) => `
    <article class="overview-card">
      <h3>${title}</h3>
      <p>${text}</p>
    </article>
  `).join("");
  byId("automation-cards").innerHTML = t.automationCards.map(([title, text]) => `
    <article class="flow-card">
      <h3>${title}</h3>
      <p>${text}</p>
    </article>
  `).join("");
}

function renderStats() {
  const stats = state.data.stats;
  const t = ui[state.lang];
  const items = [
    [stats.works, t.stats.works],
    [stats.topics, t.stats.topics],
    [stats.domains, t.stats.domains],
    [stats.activities, t.stats.activities],
    [stats.monthly_reports, t.stats.monthlyReports],
  ];
  byId("stats").innerHTML = items.map(([value, label]) => `
    <article class="stat-card">
      <span class="value">${value}</span>
      <span>${label}</span>
    </article>
  `).join("");
}

function fillSelect(id, label, items) {
  const select = byId(id);
  const key = id.replace("-filter", "");
  const current = state.filters[key] || "";
  const t = ui[state.lang];
  select.innerHTML = `<option value="">${t.filters[label]}</option>` + items.map(item => `
    <option value="${item.slug || item.month}">${item.name ? localizedItemName(item) : item.month}</option>
  `).join("");
  select.value = current;
}

function axisCard(item, kind) {
  const label = state.lang === "en" ? `${item.count} works` : `${item.count} 项 work`;
  const name = localizedItemName(item);
  const href = localizedItemUrl(item);
  return `
    <article class="axis-card">
      <h3><a href="${href}" data-reader-link="true" data-reader-title="${escapeHtml(name)}">${name}</a></h3>
      <p class="metric">${label}</p>
      <p class="mini-note">${kind}</p>
      <a href="${href}" data-reader-link="true" data-reader-title="${escapeHtml(name)}">${ui[state.lang].openPage}</a>
    </article>
  `;
}

function renderTopics() {
  byId("topics-grid").innerHTML = state.data.topics.map(item =>
    axisCard(item, state.lang === "en" ? "Evaluation problem" : "评估问题")
  ).join("");
}

function renderDomains() {
  byId("domains-grid").innerHTML = state.data.domains.map(item =>
    axisCard(item, state.lang === "en" ? "Field view" : "领域入口")
  ).join("");
}

function renderActivities() {
  byId("activities-grid").innerHTML = state.data.activities.map(item =>
    axisCard(item, state.lang === "en" ? "Task view" : "任务入口")
  ).join("");
}

function renderTimeline() {
  const max = Math.max(...state.data.timeline.map(item => item.count), 1);
  byId("timeline").innerHTML = state.data.timeline.slice().reverse().map(item => `
    <button class="timeline-row ${state.filters.month === item.month ? "is-active" : ""}" data-month="${item.month}" type="button">
      <span>${item.month}</span>
      <span class="bar-wrap"><span class="bar" style="width:${(item.count / max) * 100}%"></span></span>
      <span>${item.count}</span>
    </button>
  `).join("");
  byId("timeline").querySelectorAll("button").forEach(button => {
    button.addEventListener("click", () => {
      state.filters.month = button.dataset.month === state.filters.month ? "" : button.dataset.month;
      byId("month-filter").value = state.filters.month;
      renderTimeline();
      renderMonthlyReports();
      renderResults();
      setActiveTab("monthly");
    });
  });
}

function monthlyCard(item) {
  const title = state.lang === "en" ? item.title : (item.zh_title || item.title);
  const summary = state.lang === "en" ? item.summary : (item.zh_summary || item.summary);
  const href = state.lang === "en" ? item.url : item.zh_url;
  return `
    <article class="monthly-card">
      <h3><a href="${href}" data-reader-link="true" data-reader-title="${escapeHtml(title)}">${title}</a></h3>
      <p class="metric">${ui[state.lang].monthlyWorks(item.works_count)}</p>
      <p>${summary}</p>
    </article>
  `;
}

function renderMonthlyReports() {
  const reports = state.filters.month
    ? state.data.monthly_reports.filter(item => item.month === state.filters.month)
    : state.data.monthly_reports;
  byId("monthly-reports").innerHTML = reports.map(monthlyCard).join("");
  byId("home-monthly-reports").innerHTML = state.data.monthly_reports.slice(0, 3).map(monthlyCard).join("");
}

function filterWorks() {
  const q = state.filters.search.trim().toLowerCase();
  return state.data.works.filter(work => {
    const matchesSearch = !q || [
      work.title,
      work.overview,
      work.summary,
      (work.zh && work.zh.overview) || "",
      (work.zh && work.zh.summary) || ""
    ].join(" ").toLowerCase().includes(q);
    const matchesTopic = !state.filters.topic || work.topics.some(item => item.slug === state.filters.topic);
    const matchesDomain = !state.filters.domain || work.domains.some(item => item.slug === state.filters.domain);
    const matchesActivity = !state.filters.activity || work.activities.some(item => item.slug === state.filters.activity);
    const matchesMonth = !state.filters.month || work.first_appeared_month === state.filters.month;
    return matchesSearch && matchesTopic && matchesDomain && matchesActivity && matchesMonth;
  });
}

function tagRow(label, items) {
  if (!items.length) return "";
  return `
    <div class="tag-row">
      <span class="tag"><strong>${ui[state.lang][label]}:</strong></span>
      ${items.map(item => {
        const name = localizedItemName(item);
        return `<a class="tag" href="${localizedItemUrl(item)}" data-reader-link="true" data-reader-title="${escapeHtml(name)}">${name}</a>`;
      }).join("")}
    </div>
  `;
}

function renderResults() {
  const works = filterWorks();
  const t = ui[state.lang];
  setText("results-count", t.resultsCount(works.length));
  byId("results").innerHTML = works.slice(0, 40).map(work => {
    const blurb = state.lang === "en" ? work.overview : (((work.zh && work.zh.overview) || work.overview));
    const summary = state.lang === "en" ? work.summary : (((work.zh && work.zh.summary) || work.summary));
    const href = state.lang === "en" ? work.card_url : work.zh_card_url;
    const links = work.links.map(link => `<a class="tag" href="${link.url}" target="_blank" rel="noopener noreferrer">${link.label}</a>`).join("");
    return `
      <article class="work-card">
        <h3><a href="${href}" data-reader-link="true" data-reader-title="${escapeHtml(work.title)}">${work.title}</a></h3>
        <div class="card-meta">
          <span>${t.firstAppeared}: ${work.first_appeared}</span>
          <span>${t.source}: <a href="${localizedDocumentUrl(work.first_appeared_source.url)}">${work.first_appeared_source.label}</a></span>
        </div>
        <p>${blurb}</p>
        <p>${summary}</p>
        ${tagRow("topics", work.topics)}
        ${tagRow("domains", work.domains)}
        ${tagRow("activities", work.activities)}
        <div class="tag-row">
          <span class="tag"><strong>${t.links}:</strong></span>
          ${links}
        </div>
      </article>
    `;
  }).join("");
}

function setActiveTab(tab) {
  state.activeTab = tab;
  document.querySelectorAll(".tab").forEach(node => {
    node.classList.toggle("is-active", node.dataset.tab === tab);
  });
  document.querySelectorAll(".tab-panel").forEach(node => {
    node.classList.toggle("is-active", node.dataset.panel === tab);
  });
}

function escapeHtml(text) {
  return String(text)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

function isLocalDocumentLink(href) {
  const url = new URL(href, window.location.href);
  return url.origin === window.location.origin && /\/documents\/(?:en|zh)\/.+\.json$/.test(url.pathname);
}

function resolveDocumentLink(href, sourcePath) {
  if (!sourcePath || /^https?:\/\//.test(href) || href.startsWith("#")) return href;
  const [pathPart, fragment] = href.split("#", 2);
  if (!/\.md$/.test(pathPart)) return href;
  const resolved = new URL(pathPart, `https://documents.invalid/${sourcePath}`).pathname.slice(1);
  const document = state.data.documents[resolved];
  if (!document) return href;
  const url = state.lang === "zh" ? document.zh_url : document.url;
  return fragment ? `${url}#${fragment}` : url;
}

function renderInline(text, sourcePath) {
  let html = escapeHtml(text);
  html = html.replace(/`([^`]+)`/g, "<code>$1</code>");
  html = html.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
  html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, (m, label, href) => {
    const safeLabel = label;
    const resolvedHref = resolveDocumentLink(href, sourcePath);
    const safeHref = isLocalDocumentLink(resolvedHref) ? localizedDocumentUrl(resolvedHref) : resolvedHref;
    if (isLocalDocumentLink(safeHref)) {
      return `<a href="${safeHref}" data-reader-link="true" data-reader-title="${escapeHtml(safeLabel)}">${safeLabel}</a>`;
    }
    const attrs = /^https?:\/\//.test(safeHref) ? ' target="_blank" rel="noopener noreferrer"' : "";
    return `<a href="${safeHref}"${attrs}>${safeLabel}</a>`;
  });
  return html;
}

function renderMarkdown(md, sourcePath) {
  const languageLink = String.raw`(?:\*\*(?:English|简体中文)\*\*|\[(?:English|简体中文)\]\([^)]+\))`;
  const languageSwitcher = new RegExp(`^>\\s*${languageLink}\\s*\\|\\s*${languageLink}(?:\\s*·.*)?$`);
  const lines = md.replace(/\r\n/g, "\n").split("\n").filter(line => !languageSwitcher.test(line.trim()));
  let html = "";
  let i = 0;

  function flushParagraph(buffer) {
    if (!buffer.length) return "";
    const text = buffer.join(" ").trim();
    return text ? `<p>${renderInline(text, sourcePath)}</p>` : "";
  }

  while (i < lines.length) {
    const line = lines[i];
    if (!line.trim()) {
      i += 1;
      continue;
    }

    if (/^```/.test(line)) {
      const fence = line;
      const code = [];
      i += 1;
      while (i < lines.length && !lines[i].startsWith("```")) {
        code.push(lines[i]);
        i += 1;
      }
      i += 1;
      html += `<pre><code>${escapeHtml(code.join("\n"))}</code></pre>`;
      continue;
    }

    if (/^#{1,6}\s/.test(line)) {
      const level = line.match(/^#+/)[0].length;
      html += `<h${level}>${renderInline(line.replace(/^#{1,6}\s+/, ""), sourcePath)}</h${level}>`;
      i += 1;
      continue;
    }

    if (/^>\s?/.test(line)) {
      const quote = [];
      while (i < lines.length && /^>\s?/.test(lines[i])) {
        quote.push(lines[i].replace(/^>\s?/, ""));
        i += 1;
      }
      html += `<blockquote>${renderMarkdown(quote.join("\n"), sourcePath)}</blockquote>`;
      continue;
    }

    if (/^---+$/.test(line.trim())) {
      html += "<hr>";
      i += 1;
      continue;
    }

    if (/^\|/.test(line) && i + 1 < lines.length && /^\|?(?:\s*:?-+:?\s*\|)+\s*$/.test(lines[i + 1])) {
      const tableLines = [line, lines[i + 1]];
      i += 2;
      while (i < lines.length && /^\|/.test(lines[i])) {
        tableLines.push(lines[i]);
        i += 1;
      }
      const rows = tableLines.map(row => row.trim().replace(/^\||\|$/g, "").split("|").map(cell => cell.trim()));
      const header = rows[0];
      const body = rows.slice(2);
      const wideClass = header.length >= 10 ? " is-wide" : "";
      html += `<div class="table-scroll${wideClass}" role="region" aria-label="Scrollable table" tabindex="0"><table><thead><tr>` + header.map(cell => `<th>${renderInline(cell, sourcePath)}</th>`).join("") + "</tr></thead><tbody>";
      body.forEach(row => {
        html += "<tr>" + row.map(cell => `<td>${renderInline(cell, sourcePath)}</td>`).join("") + "</tr>";
      });
      html += "</tbody></table></div>";
      continue;
    }

    if (/^\s*[-*]\s+/.test(line)) {
      const items = [];
      while (i < lines.length && /^\s*[-*]\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*[-*]\s+/, ""));
        i += 1;
      }
      html += "<ul>" + items.map(item => `<li>${renderInline(item, sourcePath)}</li>`).join("") + "</ul>";
      continue;
    }

    if (/^\s*\d+\.\s+/.test(line)) {
      const items = [];
      while (i < lines.length && /^\s*\d+\.\s+/.test(lines[i])) {
        items.push(lines[i].replace(/^\s*\d+\.\s+/, ""));
        i += 1;
      }
      html += "<ol>" + items.map(item => `<li>${renderInline(item, sourcePath)}</li>`).join("") + "</ol>";
      continue;
    }

    const paragraph = [];
    while (
      i < lines.length &&
      lines[i].trim() &&
      !/^#{1,6}\s/.test(lines[i]) &&
      !/^```/.test(lines[i]) &&
      !/^>\s?/.test(lines[i]) &&
      !/^\|/.test(lines[i]) &&
      !/^\s*[-*]\s+/.test(lines[i]) &&
      !/^\s*\d+\.\s+/.test(lines[i]) &&
      !/^---+$/.test(lines[i].trim())
    ) {
      paragraph.push(lines[i]);
      i += 1;
    }
    html += flushParagraph(paragraph);
  }

  return html;
}

async function openReader(url, title) {
  const response = await fetch(url);
  if (!response.ok) {
    byId("reader-content").innerHTML = `<p>Failed to load ${escapeHtml(url)} (${response.status}).</p>`;
    state.reader = { url, title: title || url };
    setActiveTab("reader");
    applyUiText();
    return;
  }
  const document = await response.json();
  state.reader = { url, title: title || url };
  byId("reader-content").classList.remove("reader-empty");
  byId("reader-content").innerHTML = renderMarkdown(document.markdown, document.source_path);
  setActiveTab("reader");
  applyUiText();
}

function handleReaderClick(event) {
  const link = event.target.closest("a");
  if (!link) return;
  const href = link.getAttribute("href");
  if (link.dataset.readerLink !== "true" && !isLocalDocumentLink(href)) return;
  event.preventDefault();
  const url = localizedDocumentUrl(href);
  const title = link.getAttribute("data-reader-title") || link.textContent.trim();
  openReader(url, title);
}

function bindControls() {
  document.addEventListener("click", handleReaderClick);
  document.querySelectorAll(".tab").forEach(button => {
    button.addEventListener("click", () => setActiveTab(button.dataset.tab));
  });
  byId("search").addEventListener("input", (event) => {
    state.filters.search = event.target.value;
    renderResults();
  });
  ["topic", "domain", "activity", "month"].forEach(name => {
    byId(`${name}-filter`).addEventListener("change", (event) => {
      state.filters[name] = event.target.value;
      renderResults();
      if (name === "month") {
        renderTimeline();
        renderMonthlyReports();
      }
    });
  });
  byId("lang-toggle").addEventListener("click", () => {
    state.lang = state.lang === "en" ? "zh" : "en";
    localStorage.setItem("scieval-explorer-language", state.lang);
    applyUiText();
    renderHomeBlocks();
    renderStats();
    fillSelect("topic-filter", "allTopics", state.data.topics);
    fillSelect("domain-filter", "allDomains", state.data.domains);
    fillSelect("activity-filter", "allActivities", state.data.activities);
    fillSelect("month-filter", "allMonths", state.data.timeline);
    renderTopics();
    renderDomains();
    renderActivities();
    renderTimeline();
    renderMonthlyReports();
    renderResults();
    if (state.activeTab === "reader" && state.reader.url) {
      openReader(localizedDocumentUrl(state.reader.url), state.reader.title);
    }
  });
}

async function main() {
  const response = await fetch("./data/index.json");
  state.data = await response.json();
  applyUiText();
  renderHomeBlocks();
  renderStats();
  fillSelect("topic-filter", "allTopics", state.data.topics);
  fillSelect("domain-filter", "allDomains", state.data.domains);
  fillSelect("activity-filter", "allActivities", state.data.activities);
  fillSelect("month-filter", "allMonths", state.data.timeline);
  renderTopics();
  renderDomains();
  renderActivities();
  renderTimeline();
  renderMonthlyReports();
  renderResults();
  bindControls();
  byId("reader-content").innerHTML = `<p>${ui[state.lang].readerEmpty}</p>`;
}

main();
