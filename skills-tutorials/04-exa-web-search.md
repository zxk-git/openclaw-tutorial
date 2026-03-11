<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>

---
[⬅️ 上一篇：DDG Web Search](03-ddg-web-search.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：File Search](05-file-search.md)
---

# Exa Web Search (Free) — 免费 AI 神经搜索

> **版本**: 1.0.1 | **Slug**: `exa-web-search-free` | **难度**: ⭐⭐

---

## 📖 简介

免费 AI 神经搜索引擎，支持网页搜索、代码搜索和企业研究。通过 Exa MCP 服务提供，无需管理 API Key，配合 McPorter 使用。

---

## 📦 安装

```bash
clawdhub install exa-web-search-free
```

### 前置依赖

需要先安装 [McPorter](01-mcporter.md)：

```bash
clawdhub install mcporter
```

---

## ⚙️ 首次配置

```bash
# 添加 Exa MCP 服务
mcporter config add exa https://mcp.exa.ai/mcp

# 认证
mcporter auth exa
```

---

## 🔧 三大核心工具

### 1. 网页搜索 (web_search_exa)

```bash
mcporter call 'exa.web_search_exa(query: "OpenClaw tutorial", numResults: 5)'
```

**搜索模式**：
| 模式 | 说明 |
|------|------|
| `fast` | 快速搜索，适合简单查询 |
| `deep` | 深度搜索，结果更全面 |
| `auto` | 自动选择最优模式 |

### 2. 代码搜索 (get_code_context_exa)

```bash
mcporter call 'exa.get_code_context_exa(query: "React hooks best practices", tokensNum: 3000)'
```

搜索覆盖：GitHub、Stack Overflow、技术博客等。

### 3. 企业研究 (company_research_exa)

```bash
mcporter call 'exa.company_research_exa(companyName: "OpenAI", numResults: 3)'
```

---

## 🛠️ 高级工具（可扩展）

| 工具 | 功能 |
|------|------|
| 域名过滤搜索 | 限定搜索特定网站 |
| 全页抓取 | 获取完整页面内容 |
| 人物搜索 | 搜索特定人物的公开信息 |
| AI 深度研究 | 多轮搜索综合研究 |

---

## 💡 使用场景

| 场景 | 推荐工具 |
|------|----------|
| 找技术文档 | `web_search_exa` + fast 模式 |
| 找代码示例 | `get_code_context_exa` |
| 调研竞品 | `company_research_exa` |
| 深度研究 | `web_search_exa` + deep 模式 |

---

## ❓ 常见问题

**Q: 调用报错 "server not found"？**
运行 `mcporter config add exa https://mcp.exa.ai/mcp` 添加服务器配置。

**Q: 与 Tavily Search 有什么区别？**
Exa 免费但通过 MCP 调用；Tavily 需要 API Key，但结果更适合 AI 消费。推荐搭配使用。

---

<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>
