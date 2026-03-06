# 第4章：Skills 安装与管理实践

> 本章介绍如何安装、管理和维护 OpenClaw Skills，包括从 ClawdHub 安装、手动安装、版本管理和安全审查。

---

## 4.1 Skills 安装方式

OpenClaw 提供多种 Skill 安装方式，适应不同场景。

### 方式一：ClawdHub 安装（推荐）

ClawdHub 是 OpenClaw 的官方技能市场，提供经过审核的 Skills：

```bash
clawdhub install tavily-search
clawdhub install memory
clawdhub install proactive-agent
```

### 方式二：npx skills CLI

```bash
# 搜索技能
npx skills find "web search"

# 安装技能
npx skills add tavily-search

# 检查更新
npx skills check

# 批量更新
npx skills update
```

### 方式三：手动安装

从 GitHub 或其他来源手动安装：

```bash
git clone https://github.com/author/my-skill.git \
  ~/.openclaw/workspace/skills/my-skill
```

### 方式四：MCP 工具集成

通过 McPorter 添加 MCP 服务器（可提供工具级 Skill）：

```bash
mcporter config add exa https://mcp.exa.ai/mcp
mcporter config add xiaohongshu http://localhost:18060/mcp
```

---

## 4.2 Skills 发现与搜索

如何找到需要的 Skills。

### ClawdHub 浏览

访问 [https://skills.sh](https://skills.sh/) 在线浏览所有可用技能。

### 命令行搜索

```bash
# 搜索包含关键词的技能
npx skills find "search"
npx skills find "automation"
npx skills find "feishu"
```

### 本地已安装列表

```bash
ls ~/.openclaw/workspace/skills/
# 详细信息
for dir in ~/.openclaw/workspace/skills/*/; do
  name=$(basename "$dir")
  if [ -f "$dir/SKILL.md" ]; then
    desc=$(grep -oP 'description:\s*"\K[^"]+' "$dir/SKILL.md" | head -1)
    echo "  📦 $name: $desc"
  fi
done
```

---

## 4.3 版本管理

Skills 支持语义化版本管理。

### 查看当前版本

```bash
# 查看单个 Skill 版本
head -10 ~/.openclaw/workspace/skills/tavily-search/SKILL.md

# 查看所有 Skill 版本
npx skills check
```

### 更新策略

```bash
# 检查可用更新
npx skills check

# 更新所有
npx skills update

# 更新指定 Skill
npx skills update tavily-search
```

### 版本回退

手动安装的 Skills 支持 Git 回退：

```bash
cd ~/.openclaw/workspace/skills/my-skill
git log --oneline
git checkout v1.0.0  # 回退到指定版本
```

---

## 4.4 安全审查

安装第三方 Skills 前应进行安全审查。OpenClaw 内置了 `skill-vetter` 技能，专门用于安全检查。

### skill-vetter 审查流程

1. **来源检查** — 验证 Skill 来源是否可信
2. **代码审查 (MANDATORY)** — 检查脚本中的危险操作
3. **权限范围** — 评估 Skill 访问的系统资源
4. **红旗检测** — 扫描可疑模式（如 `rm -rf`, `eval`, 网络外泄等）

### 使用方法

在安装前，让 Agent 对 Skill 进行审查：

```
请帮我审查这个 Skill: https://github.com/author/suspect-skill
```

### 安全配置

OpenClaw 提供执行审批机制：

```json
// ~/.openclaw/exec-approvals.json
{
  "autoApprove": ["ls", "cat", "echo"],
  "requireApproval": ["rm", "curl", "wget"],
  "deny": ["rm -rf /"]
}
```

### 最佳实践

- 优先使用 ClawdHub 官方审核的 Skills
- 安装前阅读 SKILL.md 了解权限范围
- 对包含 `scripts/` 的 Skills 检查脚本内容
- 定期运行 `npx skills check` 检查更新

---

## 4.5 Skill 配置与 openclaw.json

部分 Skills 需要在主配置文件中配置。

### 技能启用/禁用

```json
// ~/.openclaw/openclaw.json
{
  "skills": {
    "entries": {
      "tavily": {
        "enabled": true,
        "apiKey": "tvly-xxx"
      },
      "ddg-search": {
        "enabled": true
      },
      "notion": {
        "enabled": false
      }
    }
  }
}
```

### 需要 API Key 的 Skills

| Skill | 环境变量 | 获取方式 |
|-------|---------|---------|
| tavily-search | `TAVILY_API_KEY` | https://tavily.com |
| notion | `NOTION_KEY` | https://developers.notion.com |
| gog | Google OAuth | `gog auth` |

### MCP 服务器配置

通过 McPorter 管理的 MCP 型 Skill：

```bash
# 查看已配置的 MCP 服务器
mcporter list

# 添加新服务器
mcporter config add <name> <url>

# 调用 MCP 工具
mcporter call 'exa.web_search_exa(query: "AI agents")'
```

---

## 4.6 实战：搭建搜索技能组合

以搭建完整的搜索能力为例，展示 Skills 安装管理实战。

### 目标
构建多引擎搜索能力：Tavily（主力）→ DuckDuckGo（免费备选）→ Exa（MCP）

### Step 1：安装搜索 Skills

```bash
# 安装 Tavily（需要 API Key）
clawdhub install tavily-search
# 配置 API Key
# 编辑 ~/.openclaw/openclaw.json → skills.entries.tavily.apiKey

# 安装 DuckDuckGo（零依赖）
clawdhub install ddg-web-search

# 安装 Exa MCP
mcporter config add exa https://mcp.exa.ai/mcp
```

### Step 2：验证安装

```bash
# 测试 Tavily
node ~/.openclaw/workspace/skills/tavily-search/scripts/search.mjs "test"

# 测试 DuckDuckGo
curl -sL "https://lite.duckduckgo.com/lite/?q=test&kl=au-en"

# 测试 Exa
mcporter call 'exa.web_search_exa(query: "test", numResults: 3)'
```

### Step 3：配置优先级

Agent 会根据 SKILL.md 的 triggers 和上下文自动选择合适的搜索引擎。可在对话中指定：

```
搜索 "OpenClaw 教程"              ← Agent 自动选择
用 Tavily 搜索 "OpenClaw 教程"    ← 指定引擎
```

---

## 常见问题

| 问题 | 解决方法 |
|------|---------|
| 安装后 Skill 不生效 | 重启 Agent 或开始新会话，确认 SKILL.md 存在于 skills/ 目录下 |
| API Key 配置在哪 | 在 `~/.openclaw/openclaw.json` 的 `skills.entries` 中，或设置环境变量 |
| 如何卸载 Skill | 删除对应目录：`rm -rf ~/.openclaw/workspace/skills/<name>` |
| MCP 服务器连接失败 | 运行 `mcporter list` 检查状态，确认 URL 可达 |

---

## 本章小结

- Skills 安装与管理实践 是 OpenClaw 平台的重要功能。
- Skills 安装方式：掌握其核心概念和操作方法。
- Skills 发现与搜索：掌握其核心概念和操作方法。
- 版本管理：掌握其核心概念和操作方法。
- 安全审查：掌握其核心概念和操作方法。
- Skill 配置与 openclaw.json：掌握其核心概念和操作方法。
- 遇到问题时，善用 `openclaw doctor` 进行诊断。

> 下一章：ClawHub 平台与技能分发
