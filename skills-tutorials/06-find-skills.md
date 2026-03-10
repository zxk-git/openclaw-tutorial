---
[⬅️ 上一篇：File Search](05-file-search.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：GitHub](07-github.md)
---

# Find Skills — 技能发现与安装助手

> **版本**: 0.1.0 | **Slug**: `find-skills` | **难度**: ⭐

---

## 📖 简介

帮助用户从开放 Agent 技能生态中发现和安装新技能。当用户询问"怎么做 X"或寻求扩展 Agent 功能时自动触发。

---

## 📦 安装

```bash
clawdhub install find-skills
```

---

## 🔧 核心用法

### 搜索技能

```bash
npx skills find "web search"
npx skills find "react performance"
npx skills find "pdf converter"
```

### 安装技能

```bash
npx skills add <owner/repo@skill>
```

### 检查更新

```bash
npx skills check
```

### 批量更新

```bash
npx skills update
```

### 浏览技能目录

在线目录：https://skills.sh/

---

## 💡 触发场景

Agent 会在以下情况自动建议搜索技能：
- 用户问"怎么搜索网页？" → 推荐搜索类技能
- 用户问"能处理 PDF 吗？" → 推荐文档处理类技能
- 用户需要的能力当前不具备时

---

## ❓ 常见问题

**Q: npx 命令不可用？**
需要安装 Node.js：`apt install nodejs npm` 或 `brew install node`。

**Q: 安装的技能放在哪里？**
统一放在 `~/.openclaw/workspace/skills/` 目录下。

---

> 📖 [返回 Skills 教程目录](README.md)
