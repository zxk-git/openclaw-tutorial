<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>

---
[⬅️ 上一篇：Notion](12-notion.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Proactive Agent](14-proactive-agent.md)
---

# PowerPoint PPTX — PowerPoint 自动化生成

> **版本**: 1.0.0 | **Slug**: `powerpoint-pptx` | **难度**: ⭐⭐

---

## 📖 简介

使用 `python-pptx` 库程序化创建、编辑和自动化 PowerPoint 演示文稿。支持 7 种内置布局，可处理文本、图表、表格和图片。

---

## 📦 安装

```bash
clawdhub install powerpoint-pptx
```

### 安装 Python 依赖

```bash
pip install python-pptx
```

---

## 🔧 核心用法

### 创建演示文稿

```python
from pptx import Presentation
from pptx.util import Inches, Pt

prs = Presentation()

# 标题页（布局 0）
slide = prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text = "项目汇报"
slide.placeholders[1].text = "2026 年 Q1 总结"

# 内容页（布局 1）
slide = prs.slides.add_slide(prs.slide_layouts[1])
slide.shapes.title.text = "核心成果"
body = slide.placeholders[1]
body.text = "完成了 18 个 Skill 教程编写"
body.text_frame.add_paragraph().text = "安全审计全部通过"

prs.save("report.pptx")
```

### 7 种内置布局

| 索引 | 布局名称 | 用途 |
|------|---------|------|
| 0 | Title Slide | 封面页 |
| 1 | Title and Content | 标题 + 正文 |
| 2 | Section Header | 章节分隔页 |
| 3 | Two Content | 左右分栏 |
| 4 | Comparison | 对比布局 |
| 5 | Title Only | 仅标题 |
| 6 | Blank | 空白页 |

### 添加表格

```python
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = "数据概览"

rows, cols = 3, 4
table = slide.shapes.add_table(rows, cols, Inches(1), Inches(2), Inches(8), Inches(3)).table

# 设置表头
table.cell(0, 0).text = "项目"
table.cell(0, 1).text = "进度"
table.cell(0, 2).text = "状态"
table.cell(0, 3).text = "负责人"

# 填充数据
table.cell(1, 0).text = "Skills 教程"
table.cell(1, 1).text = "100%"
table.cell(1, 2).text = "已完成"
table.cell(1, 3).text = "Agent"
```

### 添加图片

```python
slide = prs.slides.add_slide(prs.slide_layouts[6])
slide.shapes.add_picture("logo.png", Inches(1), Inches(1), Inches(3), Inches(3))
```

---

## 💡 使用场景

| 场景 | 做法 |
|------|------|
| 自动生成周报 | 模板 + 数据填充 |
| 批量生成演示文稿 | 循环创建幻灯片 |
| 修改现有 PPT | `Presentation("existing.pptx")` |
| 提取 PPT 内容 | 遍历 slides 和 shapes |

---

## ❓ 常见问题

**Q: 中文显示方块？**
设置字体为支持中文的字体：`run.font.name = "微软雅黑"`。

**Q: 如何使用自定义模板？**
`Presentation("template.pptx")` 加载模板，然后添加幻灯片。

---

<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>
