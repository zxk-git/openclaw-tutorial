<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>

---
[📑 Skills 教程目录](README.md) | [➡️ 下一篇：Complex Task Automator](02-complex-task-automator.md)
---

# McPorter — MCP 工具 CLI 管理器

> **版本**: 1.0.0 | **Slug**: `mcporter` | **难度**: ⭐⭐

---

## 📖 简介

McPorter 是 MCP（Model Context Protocol）服务器/工具的命令行管理器，支持在 HTTP 和 stdio 模式下列出、配置、认证和直接调用 MCP 工具。它是 OpenClaw 与外部 MCP 服务交互的核心桥梁。

---

## 📦 安装

```bash
clawdhub install mcporter
```

安装完成后，`mcporter` 命令即可在终端中使用。

---

## ⚙️ 初始配置

### 1. 查看配置文件

```bash
cat ~/.openclaw/config/mcporter.json
```

### 2. 添加 MCP 服务器

```bash
# 添加 HTTP 模式的 MCP 服务器
mcporter config add <server-name> <url>

# 示例：添加 Exa 搜索
mcporter config add exa https://mcp.exa.ai/mcp
```

### 3. OAuth 认证

```bash
mcporter auth <server-name>
```

---

## 🔧 核心用法

### 列出已配置的服务器

```bash
mcporter list
```

### 查看服务器提供的工具

```bash
mcporter list <server-name> --schema
```

### 调用工具

McPorter 支持多种调用语法：

```bash
# 选择器语法
mcporter call <server>.<tool> key=value

# 函数语法
mcporter call '<server>.<tool>(arg1: "value1", arg2: "value2")'

# 示例：调用 Exa 搜索
mcporter call 'exa.web_search_exa(query: "OpenClaw tutorial", numResults: 5)'
```

### JSON 输出

```bash
mcporter call <server>.<tool> key=value --output json
```

---

## 🛠️ 高级功能

### 守护进程管理

```bash
mcporter daemon start     # 启动后台守护进程
mcporter daemon stop      # 停止
mcporter daemon restart   # 重启
```

### 代码生成

```bash
# 生成 CLI 包装脚本
mcporter generate-cli --server <name>

# 生成 TypeScript 类型定义
mcporter generate-types --server <name>
```

---

## 💡 使用场景

| 场景 | 命令 |
|------|------|
| 查看所有可用工具 | `mcporter list <server> --schema` |
| 搜索网页 | `mcporter call 'exa.web_search_exa(query: "...")'` |
| 认证新服务 | `mcporter auth <server>` |
| JSON 机器可读输出 | `mcporter call ... --output json` |

---

## ❓ 常见问题

**Q: mcporter 命令找不到？**
确认已安装：`clawdhub install mcporter`，重启终端后重试。

**Q: 调用工具报 401 认证错误？**
运行 `mcporter auth <server>` 重新认证。

**Q: 如何查看工具的参数格式？**
使用 `mcporter list <server> --schema` 查看详细的 JSON Schema。

---

<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>
