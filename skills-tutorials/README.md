# 🦞 OpenClaw Skills 安装与使用教程

> 本目录包含 OpenClaw 全部已安装 Skills 的详细安装、配置和使用教程。

---

## 📋 Skills 总览

| # | Skill | 版本 | 简介 | 教程 |
|---|-------|------|------|------|
| 01 | McPorter | 1.0.0 | MCP 工具 CLI 管理器 | [查看](01-mcporter.md) |
| 02 | Complex Task Automator | 2.3.0 | 全链路任务自动化引擎 | [查看](02-complex-task-automator.md) |
| 03 | DDG Web Search | 1.0.0 | DuckDuckGo 零 API Key 搜索 | [查看](03-ddg-web-search.md) |
| 04 | Exa Web Search | 1.0.1 | 免费 AI 神经搜索引擎 | [查看](04-exa-web-search.md) |
| 05 | File Search | 1.0.0 | fd + ripgrep 快速文件搜索 | [查看](05-file-search.md) |
| 06 | Find Skills | 0.1.0 | 技能发现与安装助手 | [查看](06-find-skills.md) |
| 07 | GitHub | 1.0.0 | gh CLI 集成 | [查看](07-github.md) |
| 08 | GoG | 1.0.0 | Google Workspace CLI | [查看](08-gog.md) |
| 09 | Markdown Converter | 1.0.0 | 多格式转 Markdown | [查看](09-markdown-converter.md) |
| 10 | Memory | 1.0.2 | 无限分类记忆系统 | [查看](10-memory.md) |
| 11 | Multi Search Engine | 2.0.1 | 17 搜索引擎集成 | [查看](11-multi-search-engine.md) |
| 12 | Notion | 1.0.0 | Notion API 集成 | [查看](12-notion.md) |
| 13 | PowerPoint PPTX | 1.0.0 | PowerPoint 自动化生成 | [查看](13-powerpoint-pptx.md) |
| 14 | Proactive Agent | 3.1.0 | 主动预测型 Agent 架构 | [查看](14-proactive-agent.md) |
| 15 | Self-Improving Agent | 1.0.11 | 持续自我改进系统 | [查看](15-self-improving-agent.md) |
| 16 | Skill Vetter | 1.0.0 | 技能安全审核协议 | [查看](16-skill-vetter.md) |
| 17 | Summarize | 1.0.0 | 多源快速摘要工具 | [查看](17-summarize.md) |
| 18 | Tavily Search | 1.0.0 | AI 优化网页搜索 | [查看](18-tavily-search.md) |

---

## 🚀 通用安装方式

```bash
# 方式一：ClawdHub 安装（推荐）
clawdhub install <skill-slug>

# 方式二：手动安装
git clone <repo-url> ~/.openclaw/workspace/skills/<skill-name>

# 方式三：npx skills CLI
npx skills find <keyword>
npx skills add <package>

# 查看已安装 Skills
ls ~/.openclaw/workspace/skills/
```

## ⚠️ 安装前注意

建议在安装任何新 Skill 前先使用 [Skill Vetter](16-skill-vetter.md) 进行安全审查。

---

> 📖 [返回主教程目录](../README.md)
