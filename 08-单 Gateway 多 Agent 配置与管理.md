# 第8章：单 Gateway 多 Agent 配置与管理

> 本章讲解如何在单个 Gateway 下配置和管理多个 Agent，实现多项目隔离、多角色协作。

---

## 8.1 多 Agent 架构

OpenClaw 支持在单个 Gateway 下运行多个 Agent，每个 Agent 有独立的身份、记忆和技能配置。

### 架构图

```
Gateway (端口 18789)
├── Agent 1: 技术助手 (workspace-1/)
├── Agent 2: 运营助手 (workspace-2/)
└── Agent 3: 项目助手 (workspace-3/)
```

每个 Agent 拥有独立的：
- IDENTITY.md（身份）
- SOUL.md（行为准则）
- memory/（记忆）
- skills/（技能集）

---

## 8.2 Agent 配置

### 创建新 Agent

```bash
# 初始化新 Agent workspace
mkdir -p ~/.openclaw/agents/agent-2/workspace
cd ~/.openclaw/agents/agent-2/workspace

# 创建身份文件
cat > IDENTITY.md << 'EOF'
---
name: 运营助手
role: 运营数据分析与报告
style: 专业分析
---
EOF
```

### 路由配置

在 Gateway 配置中设置 Agent 路由规则，将不同渠道或用户映射到不同 Agent。

---

## 8.3 Agent 间通信

多个 Agent 可以通过共享文件或消息通道进行协作。

### 共享记忆

```
workspace/
├── shared-memory/  ← 共享目录
├── agent-1/
└── agent-2/
```

### 消息转发

Gateway 支持将消息从一个 Agent 转发到另一个 Agent 处理。

---

## 常见问题

| 问题 | 解决方法 |
|------|---------|
| Agent 之间如何隔离 | 每个 Agent 有独立的 workspace 目录，互不干扰 |
| Gateway 资源占用高 | 调整 `maxConcurrent` 限制并发 Agent 数量 |

---

## 本章小结

- 单 Gateway 多 Agent 配置与管理 是 OpenClaw 平台的重要功能。
- 多 Agent 架构：掌握其核心概念和操作方法。
- Agent 配置：掌握其核心概念和操作方法。
- Agent 间通信：掌握其核心概念和操作方法。
- 遇到问题时，善用 `openclaw doctor` 进行诊断。

> 下一章：故障排查与日志分析
