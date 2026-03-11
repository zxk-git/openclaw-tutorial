<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>

---
[⬅️ 上一篇：Proactive Agent](14-proactive-agent.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Skill Vetter](16-skill-vetter.md)
---

# Self-Improving Agent — 持续自我改进系统

> **版本**: 1.0.11 | **Slug**: `self-improving-agent` | **难度**: ⭐⭐

---

## 📖 简介

捕获学习记录、错误和修正以实现 Agent 持续改进。当命令失败、用户纠正、发现更好方法时自动记录，重要经验可提升到项目级别的知识库。

---

## 📦 安装

```bash
clawdhub install self-improving-agent
```

---

## ⚙️ 激活步骤

### 1. 创建学习文件

```bash
mkdir -p ~/.openclaw/workspace/.learnings
```

从模板创建或手动创建三个文件：

```bash
# 或直接复制模板
cp ~/.openclaw/workspace/skills/self-improving-agent/assets/LEARNINGS.md \
   ~/.openclaw/workspace/.learnings/
```

**所需文件：**
- `.learnings/LEARNINGS.md` — 修正、知识差距、最佳实践
- `.learnings/ERRORS.md` — 命令失败、异常
- `.learnings/FEATURE_REQUESTS.md` — 功能请求

### 2. 安装 Hook（可选但推荐）

```bash
# 复制 hook
cp -r ~/.openclaw/workspace/skills/self-improving-agent/hooks/openclaw \
   ~/.openclaw/hooks/self-improvement

# 启用 hook
openclaw hooks enable self-improvement
```

启用后，每次 session 启动时会自动注入自我改进提醒。

---

## 🔧 记录触发时机

| 情况 | 记录到 | 分类 |
|------|--------|------|
| 命令/操作失败 | `ERRORS.md` | — |
| 用户纠正（"不对，应该是..."） | `LEARNINGS.md` | `correction` |
| 发现知识过时 | `LEARNINGS.md` | `knowledge_gap` |
| 找到更好方法 | `LEARNINGS.md` | `best_practice` |
| 用户想要缺失功能 | `FEATURE_REQUESTS.md` | — |
| 简化/加固重复模式 | `LEARNINGS.md` | `simplify-and-harden` |

---

## 📝 记录格式

### Learning 条目

```markdown
## [LRN-20260310-001] correction

**Logged**: 2026-03-10T10:00:00+08:00
**Priority**: medium
**Status**: pending
**Area**: config

### Summary
OpenClaw hooks 需要 handler.js 而非 handler.sh

### Details
尝试使用 shell 脚本作为 hook handler，
但 OpenClaw 只识别 .js 和 .ts 格式的 handler。

### Resolution
使用 handler.js 或 handler.ts 编写 hook。
```

### Error 条目

```markdown
## [ERR-20260310-001]

**Logged**: 2026-03-10T10:00:00+08:00
**Severity**: medium
**Status**: resolved
**Area**: infra

### Error
`openclaw hooks enable` 报错 "hook not found"

### Context
尝试启用未正确安装的 hook

### Resolution
先将 hook 文件复制到 ~/.openclaw/hooks/ 目录
```

---

## 📈 经验提升机制

当学习记录被证明广泛适用时，提升到更高层级：

| 学习类型 | 提升到 | 示例 |
|---------|--------|------|
| 行为模式 | `SOUL.md` | "简洁直接，不加修饰" |
| 工作流改进 | `AGENTS.md` | "长任务使用子 agent" |
| 工具踩坑 | `TOOLS.md` | "Git push 需先配置认证" |

### 提升后标记

```markdown
**Status**: promoted
```

或如果提取为独立 Skill：
```markdown
**Status**: promoted_to_skill
**Skill-Path**: skills/skill-name
```

---

## 🔄 跨会话通信

OpenClaw 提供工具在会话间共享学习：

| 工具 | 功能 |
|------|------|
| `sessions_list` | 查看活跃/最近的会话 |
| `sessions_history` | 读取其他会话的记录 |
| `sessions_send` | 向其他会话发送学习 |
| `sessions_spawn` | 生成子 agent 后台处理 |

---

## 💡 最佳实践

1. **及时记录**：错误/学习发生时立即记录，不要拖延
2. **关联相似条目**：使用 `**See Also**` 链接相关记录
3. **定期审查**：心跳周期时审查 pending 状态的记录
4. **积极提升**：有价值的经验尽早提升到更高层级

---

## ❓ 常见问题

**Q: `.learnings/` 目录不存在？**
运行 `mkdir -p ~/.openclaw/workspace/.learnings` 创建。

**Q: Hook 启用后没有提醒？**
检查 `openclaw hooks list`，确认 self-improvement hook 状态为 `✓ ready`。

**Q: 日志文件越来越大怎么办？**
定期将 `resolved` 状态的条目归档到 `ARCHIVE.md`，保持活跃文件精简。

---

<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>
