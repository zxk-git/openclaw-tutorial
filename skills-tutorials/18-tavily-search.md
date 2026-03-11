<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>

---
[⬅️ 上一篇：Summarize](17-summarize.md) | [📑 Skills 教程目录](README.md)
---

# Tavily Search — AI 优化网页搜索

> **版本**: 1.0.0 | **Slug**: `tavily-search` | **难度**: ⭐⭐

---

## 📖 简介

AI 优化的网页搜索引擎，通过 Tavily API 返回干净、相关的内容片段（而非原始 HTML/广告），专为 AI Agent 设计。支持普通搜索、深度研究和新闻搜索。

---

## 📦 安装

```bash
clawdhub install tavily-search
```

---

## ⚙️ 配置

### 获取 API Key

1. 访问 https://tavily.com
2. 注册账号，获取 API Key
3. 设置环境变量：

```bash
export TAVILY_API_KEY="tvly-your-key-here"
```

---

## 🔧 核心用法

### 基础搜索

```bash
node ~/.openclaw/workspace/skills/tavily-search/scripts/search.mjs "Python async await tutorial"
```

### 深度研究模式

```bash
node ~/.openclaw/workspace/skills/tavily-search/scripts/search.mjs "OpenClaw architecture deep dive" --deep
```

深度模式会进行多轮搜索，综合更多信息源，适合需要深入理解的话题。

### 新闻搜索

```bash
# 搜索过去 7 天的新闻
node ~/.openclaw/workspace/skills/tavily-search/scripts/search.mjs "AI agent news" --topic news --days 7
```

### 控制结果数量

```bash
# 获取 10 条结果（最多 20）
node ~/.openclaw/workspace/skills/tavily-search/scripts/search.mjs "query" -n 10
```

### URL 内容提取

```bash
node ~/.openclaw/workspace/skills/tavily-search/scripts/extract.mjs "https://example.com/article"
```

---

## 📊 搜索模式对比

| 模式 | 速度 | 深度 | 适用场景 |
|------|------|------|---------|
| 普通模式 | 快 | 标准 | 日常查询 |
| `--deep` | 慢 | 深入 | 研究性问题 |
| `--topic news` | 快 | 时效 | 热点新闻 |

---

## 💡 与其他搜索 Skill 的对比

| 特性 | Tavily | DDG | Exa | Multi Search |
|------|--------|-----|-----|-------------|
| API Key | 需要 | 不需要 | 不需要 | 不需要 |
| 结果质量 | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ |
| AI 优化 | ✅ 专为 AI | ❌ 原始 HTML | ✅ 神经搜索 | ❌ 原始 HTML |
| 深度研究 | ✅ --deep | ❌ | ✅ deep 模式 | ❌ |
| 新闻搜索 | ✅ --topic news | ❌ | ❌ | ❌ |
| 费用 | 免费额度 + 付费 | 完全免费 | 完全免费 | 完全免费 |

**推荐搭配**：Tavily 作为主力搜索 → DDG/Multi Search 作为降级方案。

---

## 🔄 降级策略

在 Agent 使用中，推荐以下搜索降级链：

```
Tavily (AI 优化) → Exa (神经搜索) → DDG (免费降级) → Multi Search (更多引擎)
```

---

## ❓ 常见问题

**Q: 报错 "TAVILY_API_KEY not set"？**
运行 `export TAVILY_API_KEY="tvly-your-key"`，建议写入 `~/.bashrc`。

**Q: 免费额度用完了？**
切换到 DDG Web Search 或 Multi Search Engine 作为替代。

**Q: 搜索结果与预期不符？**
尝试调整查询词，或使用 `--deep` 模式获取更全面的结果。

---

<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>
