# 🧩 OpenClaw Skills 安装与使用教程

> 18 个已安装 Skills 的完整教程索引，每个教程包含安装、配置、核心用法和 FAQ。

---

## 📋 Skills 总览

| # | Skill | 版本 | 类型 | 简介 |
|---|-------|------|------|------|
| 01 | **McPorter** | 1.0.0 | MCP 工具管理 | MCP 工具 CLI 管理器 |
| 02 | **Complex Task Automator** | 2.3.0 | 任务自动化 | 全链路任务自动化引擎 |
| 03 | **DDG Web Search** | 1.0.0 | 搜索引擎 | DuckDuckGo 零 API Key 搜索 |
| 04 | **Exa Web Search** | 1.0.1 | 搜索引擎 | 免费 AI 神经搜索引擎 |
| 05 | **File Search** | 1.0.0 | 文件搜索 | fd + ripgrep 快速文件搜索 |
| 06 | **Find Skills** | 0.1.0 | 技能管理 | 技能发现与安装助手 |
| 07 | **GitHub** | 1.0.0 | 平台集成 | gh CLI 集成 |
| 08 | **GoG** | 1.0.0 | 平台集成 | Google Workspace CLI |
| 09 | **Markdown Converter** | 1.0.0 | 内容处理 | 多格式转 Markdown |
| 10 | **Memory** | 1.0.2 | 记忆系统 | 无限分类记忆系统 |
| 11 | **Multi Search Engine** | 2.0.1 | 搜索引擎 | 17 搜索引擎集成 |
| 12 | **Notion** | 1.0.0 | 平台集成 | Notion API 集成 |
| 13 | **PowerPoint PPTX** | 1.0.0 | 内容处理 | PowerPoint 自动化生成 |
| 14 | **Proactive Agent** | 3.1.0 | Agent 增强 | 主动预测型 Agent 架构 |
| 15 | **Self-Improving Agent** | 1.0.11 | Agent 增强 | 持续自我改进系统 |
| 16 | **Skill Vetter** | 1.0.0 | 安全审核 | 技能安全审核协议 |
| 17 | **Summarize** | 1.0.0 | 内容处理 | 多源快速摘要工具 |
| 18 | **Tavily Search** | 1.0.0 | 搜索引擎 | AI 优化网页搜索 |

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

## ⚠️ 安全建议

安装任何新 Skill 前，建议先通过 **Skill Vetter** 进行安全审查：

```bash
openclaw skill vet <skill-name>
```

---

## 📂 按类型分类

### 🔍 搜索类 Skills

| Skill | 特点 | 需要 API Key |
|-------|------|-------------|
| DDG Web Search | 零成本、无需注册 | ❌ |
| Exa Web Search | AI 神经搜索、免费额度 | ❌ |
| Multi Search Engine | 17 引擎聚合 | 部分 |
| Tavily Search | AI 优化搜索 | ✅ |

### 🔗 平台集成 Skills

| Skill | 集成平台 | 认证方式 |
|-------|---------|---------|
| GitHub | GitHub | gh CLI / Token |
| GoG | Google Workspace | OAuth2 |
| Notion | Notion | API Token |

### 🤖 Agent 增强 Skills

| Skill | 功能 | 工作方式 |
|-------|------|---------|
| Proactive Agent | 主动预判、上下文关联 | Prompt 注入到 HEARTBEAT.md |
| Self-Improving Agent | 自动复盘、持续改进 | Hook + .learnings/ 目录 |
| Complex Task Automator | 复杂任务分解执行 | 结构化流程 |

### 📝 内容处理 Skills

| Skill | 输入 | 输出 |
|-------|------|------|
| Summarize | 文件/URL/文本 | 结构化摘要 |
| Markdown Converter | PDF/DOCX/HTML | Markdown |
| PowerPoint PPTX | 文本/大纲 | .pptx 文件 |

### 🛠️ 工具管理 Skills

| Skill | 功能 |
|-------|------|
| McPorter | MCP Server 的安装/管理/调试 |
| File Search | 快速文件/内容搜索（fd + ripgrep） |
| Find Skills | 技能发现与智能推荐安装 |
| Skill Vetter | 新 Skill 安全审核 |
| Memory | 持久化分类记忆存取 |

---

## 📖 详细教程

每个 Skill 的详细教程请参阅仓库中的 `skills-tutorials/` 目录：

- [01-mcporter.md](../skills-tutorials/01-mcporter.md) — McPorter MCP 工具管理器
- [02-complex-task-automator.md](../skills-tutorials/02-complex-task-automator.md) — 全链路任务自动化
- [03-ddg-web-search.md](../skills-tutorials/03-ddg-web-search.md) — DuckDuckGo 搜索
- [04-exa-web-search.md](../skills-tutorials/04-exa-web-search.md) — Exa 神经搜索
- [05-file-search.md](../skills-tutorials/05-file-search.md) — 文件搜索
- [06-find-skills.md](../skills-tutorials/06-find-skills.md) — 技能发现
- [07-github.md](../skills-tutorials/07-github.md) — GitHub 集成
- [08-gog.md](../skills-tutorials/08-gog.md) — Google Workspace
- [09-markdown-converter.md](../skills-tutorials/09-markdown-converter.md) — Markdown 转换
- [10-memory.md](../skills-tutorials/10-memory.md) — 记忆系统
- [11-multi-search-engine.md](../skills-tutorials/11-multi-search-engine.md) — 多引擎搜索
- [12-notion.md](../skills-tutorials/12-notion.md) — Notion 集成
- [13-powerpoint-pptx.md](../skills-tutorials/13-powerpoint-pptx.md) — PPT 生成
- [14-proactive-agent.md](../skills-tutorials/14-proactive-agent.md) — 主动预测 Agent
- [15-self-improving-agent.md](../skills-tutorials/15-self-improving-agent.md) — 自我改进 Agent
- [16-skill-vetter.md](../skills-tutorials/16-skill-vetter.md) — 安全审核
- [17-summarize.md](../skills-tutorials/17-summarize.md) — 摘要工具
- [18-tavily-search.md](../skills-tutorials/18-tavily-search.md) — Tavily 搜索

---

> 📖 [返回主教程 Wiki](Home)
