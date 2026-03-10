---
[⬅️ 上一篇：Markdown Converter](09-markdown-converter.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Multi Search Engine](11-multi-search-engine.md)
---

# Memory — 无限分类记忆系统

> **版本**: 1.0.2 | **Slug**: `memory` | **难度**: ⭐⭐

---

## 📖 简介

为 Agent 提供无限制的分类存储记忆系统，与内置记忆系统并行运行、互不冲突。支持用户自定义分类目录和全局索引。

---

## 📦 安装

```bash
clawdhub install memory
```

---

## ⚙️ 首次配置

### 1. 运行设置向导

安装后阅读 `setup.md` 进行配置：

```bash
cat ~/.openclaw/workspace/skills/memory/assets/setup.md
```

### 2. 创建记忆目录

```bash
mkdir -p ~/memory
```

### 3. 初始化索引

创建 `~/memory/INDEX.md`：

```markdown
# Memory Index

## 目录结构

- `projects/` — 项目相关记忆
- `people/` — 人物信息
- `decisions/` — 重要决策
- `sync/` — 同步的内置记忆数据
```

---

## 🔧 核心用法

### 目录结构

```
~/memory/
├── INDEX.md           # 全局索引
├── projects/          # 项目记忆
│   ├── openclaw.md
│   └── my-app.md
├── people/            # 人物信息
│   ├── contacts.md
│   └── team.md
├── decisions/         # 决策记录
│   └── 2026-Q1.md
└── sync/              # 同步内置记忆
```

### 记录新记忆

Agent 会自动将重要信息存入对应分类：

```markdown
## 2026-03-10 — 项目决策

**Context**: 选择技术栈
**Decision**: 使用 Next.js + Tailwind
**Reason**: 团队熟悉，生态成熟
```

### 检索记忆

Agent 在需要时自动搜索记忆文件，也可以手动查询：

```bash
rg "Next.js" ~/memory/
```

---

## 💡 与 OpenClaw 内置记忆的区别

| 特性 | 内置记忆 | Memory Skill |
|------|---------|-------------|
| 存储位置 | `~/.openclaw/workspace/memory/` | `~/memory/` |
| 分类方式 | 按日期 | 按主题自定义 |
| 容量 | 受 workspace 限制 | 无限 |
| 搜索方式 | semantic search | 文件搜索 + grep |
| 适用场景 | 日常会话记录 | 长期结构化知识 |

两者并行运行，互不影响。

---

## ❓ 常见问题

**Q: 记忆文件太多怎么管理？**
定期整理 INDEX.md，归档过期内容，保持目录结构清晰。

**Q: 可以同步内置记忆到 Memory Skill 吗？**
可以，使用 `~/memory/sync/` 目录存放从内置记忆同步过来的数据。

---

> 📖 [返回 Skills 教程目录](README.md)
