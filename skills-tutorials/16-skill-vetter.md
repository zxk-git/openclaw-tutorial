<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>

---
[⬅️ 上一篇：Self-Improving Agent](15-self-improving-agent.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Summarize](17-summarize.md)
---

# Skill Vetter — 技能安全审核协议

> **版本**: 1.0.0 | **Slug**: `skill-vetter` | **难度**: ⭐⭐

---

## 📖 简介

安全优先的 AI Agent 技能审核协议。在安装任何第三方技能前，必须先进行安全检查，防止恶意代码或数据泄漏。

---

## 📦 安装

```bash
clawdhub install skill-vetter
```

---

## 🔧 审核流程

### 四步审核

| 步骤 | 内容 | 必须？ |
|------|------|--------|
| 1. 来源检查 | 验证技能来源（ClawdHub/GitHub/已知作者） | ✅ |
| 2. 代码审查 | 逐行检查所有文件 | ✅ **必须** |
| 3. 权限评估 | 评估所需的权限范围 | ✅ |
| 4. 风险分级 | 给出最终风险等级 | ✅ |

### 红旗清单

审查代码时重点关注以下模式：

| 红旗 | 风险 | 说明 |
|------|------|------|
| `curl` 到未知 URL | 数据泄漏 | 可能外传敏感信息 |
| 凭据访问 | 密钥泄漏 | 读取 API Key/Token |
| `base64` 解码 | 代码混淆 | 可能隐藏恶意逻辑 |
| `eval` / `exec` | 任意代码执行 | 极高风险 |
| 混淆代码 | 隐藏意图 | 无法审核 = 不安全 |
| 环境变量收集 | 信息泄漏 | 批量获取环境信息 |

### 权限范围评估

检查技能需要的权限：

| 权限类型 | 风险级别 |
|---------|---------|
| 只读文件 | 🟢 LOW |
| 读写本地文件 | 🟡 MEDIUM |
| 执行命令 | 🟡 MEDIUM |
| 网络访问（已知 API） | 🟡 MEDIUM |
| 网络访问（任意 URL） | 🔴 HIGH |
| 凭据/密钥访问 | 🔴 HIGH |
| 系统级操作 | ⛔ EXTREME |

---

## 📊 风险等级

| 等级 | 标识 | 操作建议 |
|------|------|---------|
| LOW | 🟢 | 安全安装 |
| MEDIUM | 🟡 | 审查后安装，监控运行 |
| HIGH | 🔴 | 需要额外审查，限制权限后安装 |
| EXTREME | ⛔ | **绝不安装** |

---

## 📝 审核报告格式

```markdown
## Skill Vetting Report

**Skill**: example-skill
**Version**: 1.0.0
**Source**: ClawdHub
**Author**: known-author

### Source Check
✅ ClawdHub verified author

### Code Review
✅ No suspicious patterns found
⚠️ Uses network access to api.example.com

### Permission Scope
- File read: ✅
- File write: ✅ (workspace only)
- Network: api.example.com only
- Commands: None

### Risk Assessment
**Level**: 🟡 MEDIUM
**Reason**: Network access limited to known API
**Recommendation**: Safe to install with monitoring
```

---

## 💡 使用场景

- 安装 ClawdHub 上不熟悉的技能前
- 安装 GitHub 上第三方技能前
- 定期审核已安装技能
- 配合 `security-audit.sh` 使用

---

## ❓ 常见问题

**Q: ClawdHub 上的技能还需要审核吗？**
建议进行基本审核。ClawdHub 提供初步筛查，但不能替代完整审核。

**Q: 如何审核已安装的技能？**
遍历 `~/.openclaw/workspace/skills/` 目录，对每个技能执行审核流程。

---

<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>
