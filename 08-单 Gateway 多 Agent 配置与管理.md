# 第8章：单 Gateway 多 Agent 配置与管理

> 本章讲解如何在单个 Gateway 下配置和管理多个 Agent，实现多项目隔离、多角色协作。这是 OpenClaw 中高级运维的核心能力。

---

## 8.1 多 Agent 架构

OpenClaw 支持在单个 Gateway 下运行多个 Agent，每个 Agent 有独立的身份、记忆和技能配置。

### 整体架构图

```
Gateway (端口 18789) ─── 统一入口
├── Agent 1: 技术助手 (workspace-1/)
│   ├── IDENTITY.md     → 技术专家身份
│   ├── SOUL.md         → 严谨分析风格
│   ├── skills/         → 编程、调试相关
│   └── memory/         → 技术笔记
├── Agent 2: 运营助手 (workspace-2/)
│   ├── IDENTITY.md     → 运营分析师身份
│   ├── SOUL.md         → 数据驱动风格
│   ├── skills/         → 数据分析相关
│   └── memory/         → 运营报告
└── Agent 3: 项目助手 (workspace-3/)
    ├── IDENTITY.md     → 项目经理身份
    ├── SOUL.md         → 结构化沟通风格
    ├── skills/         → 任务管理相关
    └── memory/         → 项目进展
```

每个 Agent 拥有完全独立的：
- **IDENTITY.md** — 身份定义（名字、角色、专长）
- **SOUL.md** — 行为准则（风格、边界、价值观）
- **memory/** — 记忆区（互不干扰）
- **skills/** — 技能集（按需配置）
- **config/** — 独立配置

### 隔离优势
- 不同 Agent 可以有不同的 AI 模型配置
- 技能冲突不会跨 Agent 影响
- 记忆和上下文完全隔离

---

## 8.2 Agent 配置与创建

### 创建新 Agent

```bash
# 1. 创建 Agent workspace 目录
mkdir -p ~/.openclaw/agents/agent-2/workspace
cd ~/.openclaw/agents/agent-2/workspace

# 2. 创建身份文件
cat > IDENTITY.md << 'EOF'
---
name: 运营助手
role: 运营数据分析与报告生成
style: 专业严谨，数据驱动
---
# 运营助手

我是一个专注于运营数据分析的 AI 助手。

## 核心能力
- 数据报表自动生成
- 竞品监控与分析
- 用户反馈整理
EOF

# 3. 创建行为准则
cat > SOUL.md << 'EOF'
## 行为准则
- 以数据说话，避免主观判断
- 报告格式清晰、结构化
- 敏感数据脱敏处理
EOF

# 4. 安装需要的 Skills
mkdir -p skills/
# 从 ClawHub 安装或从其他 Agent 复制
```

### 路由配置

在 Gateway 配置中设置 Agent 路由规则，将不同渠道或用户映射到不同 Agent。

```json
{
  "agents": {
    "agent-1": {
      "workspace": "~/.openclaw/agents/agent-1/workspace",
      "channels": ["feishu:group-tech"]
    },
    "agent-2": {
      "workspace": "~/.openclaw/agents/agent-2/workspace",
      "channels": ["feishu:group-ops"]
    }
  }
}
```

### 配置热加载

修改 Agent 配置后，Gateway 支持热加载而不中断服务：

```bash
# 发送信号触发重载
openclaw gateway reload

# 或通过 API
curl -X POST http://localhost:18789/admin/reload
```

---

## 8.3 Agent 间通信与协作

多个 Agent 可以通过共享文件或消息通道进行协作。

### 共享记忆目录

```
~/.openclaw/
├── workspace/shared-memory/     ← 所有 Agent 可访问
│   ├── project-status.json      ← 共享项目状态
│   └── team-notes.md            ← 团队笔记
├── agents/
│   ├── agent-1/workspace/       ← Agent 1 专属
│   └── agent-2/workspace/       ← Agent 2 专属
```

### 消息转发

Gateway 支持将消息从一个 Agent 转发到另一个 Agent 处理：

```json
{
  "routing": {
    "rules": [
      {"pattern": "技术问题.*", "target": "agent-1"},
      {"pattern": "运营报告.*", "target": "agent-2"},
      {"pattern": "default", "target": "agent-1"}
    ]
  }
}
```

### Agent 协作示例

场景：技术助手生成报告 → 运营助手分析数据

```bash
# Agent 1 将报告写入共享目录
echo "技术报告内容..." > ~/.openclaw/workspace/shared-memory/tech-report.md

# Agent 2 的 Cron 任务定期检查并分析
# (在 Agent 2 的 cron job 中配置)
```

---

## 8.4 资源管理与监控

### 资源限制

```json
{
  "agents": {
    "agent-1": {
      "maxConcurrent": 3,
      "memoryLimit": "512MB",
      "timeout": 300
    }
  }
}
```

### 监控命令

```bash
# 查看所有 Agent 状态
openclaw agents list

# 查看单个 Agent 详情
openclaw agents status agent-1

# 查看资源占用
openclaw agents stats
```

### 性能调优建议

| 场景 | 建议 |
|------|------|
| Agent 数量 > 5 | 增加 Gateway 内存限制 |
| 高并发请求 | 设置 maxConcurrent 限制 |
| 大量 Skills | 启用懒加载模式 |
| 记忆文件过多 | 定期归档和清理 |

---

## 常见问题

| 问题 | 解决方法 |
|------|---------|
| Agent 之间如何隔离 | 每个 Agent 有独立的 workspace 目录，拥有独立的身份、记忆和技能配置，互不干扰。Gateway 通过唯一路由规则分发请求 |
| Gateway 资源占用高 | 调整 `maxConcurrent` 限制并发 Agent 数量，启用懒加载模式，定期清理低活跃 Agent 的缓存 |
| 如何切换 Agent | 在飞书群中 @不同的 Agent 名称，或通过 API 指定 agentId 参数 |

---

## 本章小结

- 单 Gateway 多 Agent 配置与管理 是 OpenClaw 平台的重要功能。
- 多 Agent 架构：掌握其核心概念和操作方法。
- Agent 配置与创建：掌握其核心概念和操作方法。
- Agent 间通信与协作：掌握其核心概念和操作方法。
- 资源管理与监控：掌握其核心概念和操作方法。
- 遇到问题时，善用 `openclaw doctor` 进行诊断。

> 下一章：故障排查与日志分析
