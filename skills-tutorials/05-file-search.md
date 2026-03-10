---
[⬅️ 上一篇：Exa Web Search](04-exa-web-search.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Find Skills](06-find-skills.md)
---

# File Search — fd + ripgrep 快速文件搜索

> **版本**: 1.0.0 | **Slug**: `file-search` | **难度**: ⭐

---

## 📖 简介

使用 `fd`（文件名搜索）和 `rg`（ripgrep，文件内容搜索）进行超快速文件和内容检索。

---

## 📦 安装

```bash
clawdhub install file-search
```

### 安装工具依赖

```bash
# Debian/Ubuntu
apt install fd-find ripgrep

# macOS
brew install fd ripgrep

# 注意：Debian 上 fd 命令可能叫 fdfind
```

---

## 🔧 核心用法

### fd — 文件名搜索

```bash
# 按扩展名搜索
fd "\.py$" /path/to/project

# 精确文件名搜索（glob 模式）
fd -g "Cargo.toml" /path

# 按类型过滤
fd --type f "config"     # 只搜文件
fd --type d "test"       # 只搜目录

# 排除目录
fd "\.js$" --exclude node_modules

# 搜索隐藏文件
fd -H "\.env"
```

### rg — 文件内容搜索

```bash
# 基础内容搜索
rg "TODO|FIXME" /path/to/project

# 带上下文行
rg -C 3 "fn main" /path --type rust

# 正则表达式搜索
rg "import .* from" --type ts

# 只显示文件名
rg -l "password" /path

# 统计匹配数
rg -c "console\.log" --type js

# 搜索压缩文件
rg -z "error" /var/log/
```

---

## 💡 实用组合

### 搜索特定文件中的内容

```bash
# 先找文件，再搜内容
fd "\.md$" | xargs rg "TODO"

# 找到配置文件并搜索特定键
fd "config" --type f | xargs rg "port"
```

### 替换文本（rg + sed）

```bash
# 查找所有匹配
rg "old_function" --files-with-matches

# 批量替换（配合 sed）
rg -l "old_function" | xargs sed -i 's/old_function/new_function/g'
```

---

## 📊 fd vs rg 对比

| 功能 | fd | rg |
|------|----|----|
| 搜索目标 | 文件名/路径 | 文件内容 |
| 速度 | 极快 | 极快 |
| 正则支持 | ✅ | ✅ |
| 类型过滤 | --type f/d | --type rust/js/py |
| 忽略 .gitignore | 默认忽略 | 默认忽略 |

---

## ❓ 常见问题

**Q: fd 命令不存在？**
Debian/Ubuntu 上可能安装为 `fdfind`，运行 `alias fd=fdfind` 或使用 `fdfind`。

**Q: rg 搜索不到 node_modules 中的内容？**
默认遵循 `.gitignore`，使用 `rg --no-ignore` 强制搜索。

---

> 📖 [返回 Skills 教程目录](README.md)
