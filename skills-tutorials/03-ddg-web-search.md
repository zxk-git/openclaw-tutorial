<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>

---
[⬅️ 上一篇：Complex Task Automator](02-complex-task-automator.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Exa Web Search](04-exa-web-search.md)
---

# DDG Web Search — DuckDuckGo 零 API Key 搜索

> **版本**: 1.0.0 | **Slug**: `ddg-web-search` | **难度**: ⭐

---

## 📖 简介

无需 API Key，通过 DuckDuckGo Lite HTML 接口 + `web_fetch` 实现网页搜索。适合作为 Brave 搜索或 Tavily 的免费降级方案。

---

## 📦 安装

```bash
clawdhub install ddg-web-search
```

**依赖**：仅需 OpenClaw 内置的 `web_fetch` 工具，零额外安装。

---

## 🔧 基础用法

### 标准搜索

```javascript
web_fetch({
  url: "https://lite.duckduckgo.com/lite/?q=python+tutorial",
  extractMode: "text",
  maxChars: 8000
})
```

> **重要**：查询词中空格用 `+` 替代，特殊字符需 URL 编码。

### 精确短语搜索

```javascript
web_fetch({
  url: "https://lite.duckduckgo.com/lite/?q=%22exact+phrase%22",
  extractMode: "text",
  maxChars: 8000
})
```

### 区域过滤

在 URL 末尾添加 `&kl=` 参数：

| 区域 | 参数 |
|------|------|
| 美国英语 | `&kl=us-en` |
| 澳大利亚 | `&kl=au-en` |
| 德国 | `&kl=de-de` |
| 中国 | `&kl=cn-zh` |

```javascript
web_fetch({
  url: "https://lite.duckduckgo.com/lite/?q=AI+news&kl=us-en",
  extractMode: "text",
  maxChars: 8000
})
```

---

## 📋 Search-then-Fetch 工作流

推荐的两步搜索模式：

1. **搜索**：获取结果列表
2. **抓取**：对感兴趣的结果 URL 进行详细内容提取

```javascript
// 第一步：搜索获取结果列表
const results = web_fetch({
  url: "https://lite.duckduckgo.com/lite/?q=openclaw+tutorial",
  extractMode: "text",
  maxChars: 8000
})

// 第二步：抓取具体页面
const page = web_fetch({
  url: "https://example.com/article",
  extractMode: "text",
  maxChars: 15000
})
```

---

## 💡 使用技巧

- 自动跳过赞助/广告链接
- 使用 `lite.duckduckgo.com` 而非 `duckduckgo.com`（更简洁，解析更稳定）
- `maxChars` 建议设为 8000-15000，避免截断
- 与 Tavily 搭配使用：Tavily 失败时自动降级到 DDG

---

## ❓ 常见问题

**Q: 搜索结果为空？**
检查 URL 编码是否正确，空格应为 `+`，特殊字符需要编码。

**Q: 如何搜索中文内容？**
直接使用 URL 编码的中文查询词 + `&kl=cn-zh`。

---

<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>
