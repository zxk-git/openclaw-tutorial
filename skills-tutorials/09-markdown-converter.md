---
[⬅️ 上一篇：GoG](08-gog.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Memory](10-memory.md)
---

# Markdown Converter — 多格式转 Markdown

> **版本**: 1.0.0 | **Slug**: `markdown-converter` | **难度**: ⭐

---

## 📖 简介

使用 `markitdown` 将 20+ 种文件格式转换为 Markdown，包括 PDF、Word、PPT、Excel、HTML、CSV、图片、音频、YouTube 链接等。

---

## 📦 安装

```bash
clawdhub install markdown-converter
```

**运行方式**：通过 `uvx markitdown` 自动缓存依赖，零安装运行。

---

## 🔧 核心用法

### 基础转换

```bash
# PDF → Markdown
uvx markitdown input.pdf -o output.md

# Word → Markdown
uvx markitdown report.docx > report.md

# PPT → Markdown
uvx markitdown slides.pptx > slides.md

# Excel → Markdown
uvx markitdown data.xlsx > data.md

# HTML → Markdown
uvx markitdown page.html > page.md
```

### 管道输入

```bash
# 从 stdin 读取，需指定文件类型
cat document | uvx markitdown -x .pdf > output.md
curl -s https://example.com/doc.pdf | uvx markitdown -x .pdf > doc.md
```

### Azure Document Intelligence（复杂 PDF）

```bash
uvx markitdown scan.pdf -d -e "https://your-resource.cognitiveservices.azure.com/"
```

---

## 📋 支持格式

| 类别 | 格式 |
|------|------|
| 文档 | PDF, DOCX, PPTX, XLSX |
| 网页 | HTML, MHTML |
| 数据 | CSV, JSON, XML |
| 图片 | PNG, JPG, GIF, BMP |
| 音频 | MP3, WAV |
| 视频 | YouTube 链接 |
| 其他 | ZIP（递归提取） |

---

## 💡 使用场景

| 场景 | 用法 |
|------|------|
| 阅读 PDF 报告 | `uvx markitdown report.pdf` → 直接在终端查看 |
| 提取 PPT 内容 | `uvx markitdown slides.pptx > notes.md` |
| 网页内容存档 | `curl URL \| uvx markitdown -x .html > archive.md` |
| 数据文件速览 | `uvx markitdown data.xlsx` |

---

## ❓ 常见问题

**Q: uvx 命令找不到？**
安装 uv：`curl -LsSf https://astral.sh/uv/install.sh | sh`

**Q: PDF 转换结果丢失格式？**
对于复杂 PDF（扫描件、表格密集），使用 Azure DI 模式：`-d -e` 参数。

---

> 📖 [返回 Skills 教程目录](README.md)
