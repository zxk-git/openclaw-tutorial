# 第3章：Skills 插件体系与批量开发

> 本章深入讲解 OpenClaw 的 Skills 插件体系——它是平台最核心的扩展机制。通过 Skills，Agent 可以获得搜索、办公集成、安全审查等各种能力。你将学会如何理解 Skill 结构、编写自己的 SKILL.md 并进行批量开发。

---

## 3.1 Skills 插件体系概述

OpenClaw 的 Skills 插件体系是平台的灵魂。每个 Skill 是一个独立目录，包含描述文件（SKILL.md）、元数据（_meta.json）、脚本和配置。

Agent 在运行时会自动加载 `~/.openclaw/workspace/skills/` 目录下的所有已安装 Skills，根据触发词或用户意图匹配合适的技能并调用。

### Skills 体系架构

```
Agent 接收用户请求
    ↓
意图识别 → 匹配 Skill 触发词
    ↓
加载 SKILL.md → 解析指令/脚本/工具
    ↓
执行 Skill 逻辑（shell/python/MCP 等）
    ↓
返回结果给用户
```

### 当前内置分类

| 分类 | 数量 | 示例技能 |
|------|------|---------|
| 搜索引擎 | 5 | tavily-search, ddg-web-search, multi-search-engine |
| Agent 框架 | 2 | proactive-agent, self-improving-agent |
| 办公集成 | 2 | gog (Google Workspace), notion |
| 文件工具 | 2 | file-search, markdown-converter |
| 任务自动化 | 1 | complex-task-automator |
| 安全审查 | 1 | skill-vetter |
| MCP 集成 | 1 | McPorter |
| 记忆系统 | 1 | memory |

---

## 3.2 Skill 目录结构

每个 Skill 遵循统一的目录规范：

```
~/.openclaw/workspace/skills/<skill-name>/
├── SKILL.md          # 核心：技能描述与使用说明（必需）
├── _meta.json        # 元数据（安装源、版本等）
├── scripts/          # 可执行脚本
│   ├── search.mjs    # Node.js 脚本示例
│   └── core/         # Python 核心模块
├── templates/        # 配置模板
├── examples/         # 使用示例
└── hooks/            # 钩子脚本（可选）
```

### 关键文件说明

**SKILL.md** — 技能的入口文件，采用 YAML frontmatter + Markdown 正文：

```markdown
---
name: my-skill
version: 1.0.0
description: "技能的简短描述"
author: your-name
metadata:
  tags: [search, ai]
  triggers:
    - "搜索"
    - "查找"
---
# My Skill
正文说明如何使用此技能...
```

**_meta.json** — 安装元数据：

```json
{
  "name": "my-skill",
  "version": "1.0.0",
  "source": "clawdhub",
  "installedAt": "2026-03-01T00:00:00Z"
}
```

---

## 3.3 SKILL.md 编写规范

SKILL.md 是 Agent 理解和使用技能的唯一入口。编写质量直接影响技能的可用性。

### Frontmatter 字段

| 字段 | 类型 | 必需 | 说明 |
|------|------|------|------|
| `name` | string | ✅ | 技能唯一标识符 |
| `version` | string | ✅ | 语义化版本号 |
| `description` | string | ✅ | 简短描述（一行） |
| `author` | string | ✅ | 作者名称 |
| `metadata.tags` | list | - | 分类标签 |
| `metadata.triggers` | list | - | 触发关键词 |

### 正文结构建议

```markdown
# Skill Name
一句话说明用途。

## 快速开始
最小示例...

## 使用方法
### 命令/工具列表
详细 API 或命令...

## 配置
环境变量/参数...

## 依赖
- 系统要求: xxx
- 环境变量: xxx
```

### 编写技巧

- **触发词要准确**：避免过于宽泛（如"帮我"），应使用明确的动作词
- **示例要可运行**：给出完整的命令行示例
- **错误处理要说明**：列出常见错误及解决方法
- **依赖要声明**：明确需要哪些外部工具（如 `node`, `python3` 等）

---

## 3.4 Skill 开发实战

以创建一个简单的天气查询 Skill 为例，展示完整开发流程。

### Step 1：创建目录

```bash
mkdir -p ~/.openclaw/workspace/skills/weather-check
cd ~/.openclaw/workspace/skills/weather-check
```

### Step 2：编写 SKILL.md

```markdown
---
name: weather-check
version: 1.0.0
description: "查询指定城市的天气情况"
author: demo
metadata:
  tags: [weather, utility]
  triggers:
    - "天气"
    - "weather"
---
# Weather Check
查询指定城市的当前天气。

## 使用方法
\```bash
curl -s "https://wttr.in/Beijing?format=3"
\```

## 示例
- 查询北京天气: `curl -s "https://wttr.in/Beijing?format=3"`
- 查询上海天气: `curl -s "https://wttr.in/Shanghai?format=3"`
```

### Step 3：测试运行

```bash
# 直接运行Skill中的命令
curl -s "https://wttr.in/Beijing?format=3"
# 输出: Beijing: ⛅️  +22°C
```

### Step 4：验证注册

将 Skill 放入 `~/.openclaw/workspace/skills/` 后，Agent 会在下次会话中自动加载。

---

## 3.5 批量 Skill 管理

当拥有多个 Skills 时，需要高效的批量管理方法。

### 列出已安装 Skills

```bash
ls -la ~/.openclaw/workspace/skills/
# 或使用 find-skills 工具
npx skills check
```

### 批量操作脚本

```bash
#!/bin/bash
# 列出所有 Skill 及其版本
for skill_dir in ~/.openclaw/workspace/skills/*/; do
  skill_name=$(basename "$skill_dir")
  if [ -f "$skill_dir/SKILL.md" ]; then
    version=$(grep -oP 'version:\s*\K[\d.]+' "$skill_dir/SKILL.md" | head -1)
    echo "$skill_name: v${version:-unknown}"
  fi
done
```

### 批量更新

```bash
npx skills update  # 检查并更新所有已安装 Skills
```

### Skill 禁用与启用

在 `~/.openclaw/openclaw.json` 中控制：

```json
{
  "skills": {
    "entries": {
      "tavily": { "enabled": true },
      "ddg-search": { "enabled": false }
    }
  }
}
```

---

## 3.6 调试与测试

开发 Skills 时的调试方法和测试策略。

### 查看 Skill 加载状态

```bash
openclaw doctor  # 包含 Skills 加载检测
```

### 常见调试方式

1. **直接执行脚本**：测试 Skill 中的脚本能否独立运行
```bash
node ~/.openclaw/workspace/skills/tavily-search/scripts/search.mjs "test query"
```

2. **检查 YAML frontmatter**：确保格式正确
```bash
head -20 ~/.openclaw/workspace/skills/my-skill/SKILL.md
```

3. **查看 Agent 日志**：观察 Skill 匹配和执行过程
```bash
openclaw logs --follow
```

### 单元测试建议

为 Skill 添加测试脚本：

```bash
# scripts/test.sh
#!/bin/bash
echo "Testing weather-check skill..."
RESULT=$(curl -s "https://wttr.in/Beijing?format=3" 2>/dev/null)
if [ -n "$RESULT" ]; then
  echo "✅ PASS: Got result: $RESULT"
else
  echo "❌ FAIL: No result"
  exit 1
fi
```

---

## 常见问题

| 问题 | 解决方法 |
|------|---------|
| SKILL.md 格式不对怎么办 | 运行 `openclaw doctor` 检测，确保 YAML frontmatter 用 `---` 包裹且字段类型正确 |
| Skill 没有被 Agent 识别 | 检查文件路径是否在 `~/.openclaw/workspace/skills/` 下，确保 SKILL.md 存在 |
| 如何发布到 ClawdHub | 参见下一章《Skills 安装与管理实践》，使用 `npx skills add` 发布 |
| 脚本权限问题 | 对脚本添加执行权限：`chmod +x scripts/your-script.sh` |

---

## 本章小结

- Skills 插件体系与批量开发 是 OpenClaw 平台的重要功能。
- Skills 插件体系概述：掌握其核心概念和操作方法。
- Skill 目录结构：掌握其核心概念和操作方法。
- SKILL.md 编写规范：掌握其核心概念和操作方法。
- Skill 开发实战：掌握其核心概念和操作方法。
- 批量 Skill 管理：掌握其核心概念和操作方法。
- 遇到问题时，善用 `openclaw doctor` 进行诊断。

> 下一章：Skills 安装与管理实践
