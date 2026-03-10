---
[⬅️ 上一篇：Skill Vetter](16-skill-vetter.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Tavily Search](18-tavily-search.md)
---

# Summarize — 多源快速摘要工具

> **版本**: 1.0.0 | **Slug**: `summarize` | **难度**: ⭐⭐

---

## 📖 简介

CLI 快速摘要工具，支持 URL 网页、本地文件（PDF/图片/音频）和 YouTube 视频链接。支持多种 AI 模型和灵活的摘要长度控制。

---

## 📦 安装

```bash
clawdhub install summarize
```

---

## ⚙️ 配置

### 设置 AI 模型 API Key

根据使用的模型设置对应环境变量：

```bash
# Google Gemini（推荐，免费额度充足）
export GEMINI_API_KEY="your-key"

# OpenAI
export OPENAI_API_KEY="your-key"

# Anthropic
export ANTHROPIC_API_KEY="your-key"

# xAI
export XAI_API_KEY="your-key"
```

---

## 🔧 核心用法

### 摘要网页

```bash
summarize "https://example.com/article" --model google/gemini-3-flash-preview
```

### 摘要本地文件

```bash
# PDF
summarize "/path/to/report.pdf"

# 图片（OCR + 摘要）
summarize "/path/to/screenshot.png"

# 音频（转录 + 摘要）
summarize "/path/to/meeting.mp3"
```

### 摘要 YouTube 视频

```bash
summarize "https://youtu.be/xxx" --youtube auto
```

### 调整摘要长度

```bash
summarize "https://example.com" --length short    # 简短
summarize "https://example.com" --length medium   # 中等
summarize "https://example.com" --length long     # 详细
summarize "https://example.com" --length xl       # 非常详细
summarize "https://example.com" --length xxl      # 最大详细度
summarize "https://example.com" --length 500      # 自定义字符数
```

### JSON 输出

```bash
summarize "https://example.com" --json
```

---

## 🤖 支持的 AI 模型

| 提供商 | 模型示例 | 环境变量 |
|--------|---------|---------|
| Google | `google/gemini-3-flash-preview` | `GEMINI_API_KEY` |
| OpenAI | `openai/gpt-4o` | `OPENAI_API_KEY` |
| Anthropic | `anthropic/claude-sonnet` | `ANTHROPIC_API_KEY` |
| xAI | `xai/grok` | `XAI_API_KEY` |

---

## 💡 使用场景

| 场景 | 命令 |
|------|------|
| 快速阅读长文章 | `summarize "URL" --length short` |
| PDF 报告摘要 | `summarize "file.pdf" --length long` |
| 看 YouTube 不想看完 | `summarize "youtu.be/xxx" --youtube auto` |
| 批量处理多篇文章 | 脚本循环调用 |

---

## 🔄 备用内容提取方案

当默认提取失败时，自动尝试：
1. **Firecrawl** — 动态渲染页面
2. **Apify** — 更强大的网页抓取

---

## ❓ 常见问题

**Q: 报错 "API key not set"？**
设置对应模型的 API Key 环境变量。

**Q: YouTube 摘要失败？**
确认视频有字幕/转录。使用 `--youtube auto` 自动选择最佳方式。

**Q: 长文档摘要不完整？**
增加 `--length` 参数值或使用 `xxl`。

---

> 📖 [返回 Skills 教程目录](README.md)
