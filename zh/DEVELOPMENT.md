# 开发环境

[English](../DEVELOPMENT.md)

使用 Python 3.11 或更新版本（CI 使用 3.11），以及用于网站语法检查的 Node.js。在仓库根目录执行：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-dev.txt
python -m pytest tests/ -q
python scripts/update_counts.py --check
python scripts/monthly_report.py validate-all
node --check site/app.js
```

`requirements.txt` 固定直接运行依赖的版本；`requirements-dev.txt` 加入测试工具。GitHub Actions 使用同一组文件安装依赖，升级时在这些文件中统一修改版本。网站导出本身只依赖 Python 标准库。

本地确定性测试不需要凭据。联网检索和内容生成还需要 Claude Code CLI 和[自动更新指南](../automation/update_agent/README.md)所列凭据。不要把凭据写进仓库。
