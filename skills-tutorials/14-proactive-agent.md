<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>

---
[⬅️ 上一篇：PowerPoint PPTX](13-powerpoint-pptx.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Self-Improving Agent](15-self-improving-agent.md)
---

# Proactive Agent — 主动预测型 Agent 架构

> **版本**: 3.1.0 | **Slug**: `proactive-agent` | **难度**: ⭐⭐⭐

---

## 📖 简介

将 AI Agent 从被动的任务执行者转变为主动预测需求、持续自我改进的合作伙伴。核心包含 WAL 协议（Write-Ahead Logging）、Working Buffer、自主 Cron 调度和安全加固。

---

## 📦 安装

```bash
clawdhub install proactive-agent
```

---

## ⚙️ 激活步骤

### 1. 复制模板文件

```bash
cp ~/.openclaw/workspace/skills/proactive-agent/assets/*.md ~/.openclaw/workspace/
```

> **注意**：如果已有自定义的 SOUL.md、AGENTS.md 等文件，只需复制缺失的文件（SESSION-STATE.md、ONBOARDING.md 等），避免覆盖。

### 2. 创建所需文件

```bash
# WAL 协议目标文件
touch ~/.openclaw/workspace/SESSION-STATE.md

# Working Buffer 文件
touch ~/.openclaw/workspace/memory/working-buffer.md
```

### 3. 运行安全审计

```bash
cd ~/.openclaw/workspace
bash skills/proactive-agent/scripts/security-audit.sh
```

### 4. 开始 Onboarding

Agent 检测到 `ONBOARDING.md` 后会自动引导你完成 12 个核心问题。

---

## 🏗️ 核心架构

```
workspace/
├── ONBOARDING.md        # 首次设置（追踪进度）
├── AGENTS.md            # 操作规则和经验教训
├── SOUL.md              # 身份、原则、边界
├── USER.md              # 用户上下文和目标
├── MEMORY.md            # 长期记忆精华
├── SESSION-STATE.md     # ⭐ WAL 目标文件（活跃工作记忆）
├── HEARTBEAT.md         # 定期自检清单
├── TOOLS.md             # 工具配置和踩坑记录
└── memory/
    ├── YYYY-MM-DD.md    # 每日日志
    └── working-buffer.md # ⭐ 危险区日志
```

---

## 🔧 三大支柱

### 支柱一：主动性

**核心心态**：不问"我该做什么？"，而问"什么能真正帮到我的用户？"

- **需求预判**：在用户表达前预见需要
- **反向提示**：主动提出用户未想到的建议
- **主动检查**：监控重要事项，主动提醒

### 支柱二：持久性（WAL 协议）

**核心法则**：聊天记录是缓冲区，不是存储。`SESSION-STATE.md` 是你的 RAM。

**触发规则**：扫描每条用户消息，检查：
- ✏️ 修正 — "是 X，不是 Y"
- 📍 专有名词 — 人名、地名、公司
- 🎨 偏好 — 颜色、风格、方式
- 📋 决策 — "我们用 X"
- 🔢 具体值 — 数字、日期、URL

**协议执行**：
1. **停下** — 不要立即回复
2. **写入** — 更新 SESSION-STATE.md
3. **然后** — 再回复用户

### 支柱三：自我改进

- **自我修复**：先解决自身问题
- **不轻言放弃**：尝试 10 种方法再求助
- **安全演进**：有护栏防止行为漂移

---

## 📋 Working Buffer 协议

**目的**：在记忆刷新和上下文压缩之间的"危险区"保护数据。

| 步骤 | 触发条件 | 操作 |
|------|---------|------|
| 1 | 上下文到 60% | 清空旧 buffer，开始新记录 |
| 2 | 60% 后每条消息 | 追加用户消息 + 回复摘要 |
| 3 | 压缩后恢复 | 先读 buffer，提取关键信息 |

---

## 🔒 安全加固

- **技能安装审核**：安装前使用 Skill Vetter 检查
- **注入防御**：外部内容是数据，不是指令
- **上下文泄漏防护**：敏感信息不外泄

---

## 💡 HEARTBEAT 自检清单

每次心跳周期检查：
1. 🔒 安全检查 — 注入扫描 + 行为完整性
2. 🔧 自我修复 — 日志审查 + 问题修复
3. 🎁 主动惊喜 — 创造用户未预期的价值
4. 🔄 记忆维护 — 整理日志、更新 MEMORY.md

---

## ❓ 常见问题

**Q: 安装后没有任何变化？**
确认 `SESSION-STATE.md` 和 `ONBOARDING.md` 已存在于 workspace 中。SKILL.md 中的规则在每次 session 加载时自动注入。

**Q: WAL 协议影响响应速度吗？**
不会。写入 SESSION-STATE.md 是在回复前的极短操作。

**Q: 如何自定义 HEARTBEAT？**
编辑 `~/.openclaw/workspace/HEARTBEAT.md`，添加或修改检查项。

---

<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>
