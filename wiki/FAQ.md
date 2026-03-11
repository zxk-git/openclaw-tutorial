# ❓ 常见问题（FAQ）

> 汇集 OpenClaw 使用过程中最常遇到的问题与解决方案

---

## 📋 目录

| 分类 | 问题数 | 快速跳转 |
|------|--------|---------|
| 🔧 安装与部署 | 3 | [→ 安装与部署](#安装与部署) |
| 🧩 Skills 开发 | 3 | [→ Skills 开发](#skills-开发) |
| ⚙️ 自动化与集成 | 3 | [→ 自动化与集成](#自动化与集成) |
| 🔍 故障排查 | 2 | [→ 故障排查](#故障排查) |
| 🔒 安全与权限 | 3 | [→ 安全与权限](#安全与权限) |
| 🧠 Memory 记忆系统 | 2 | [→ Memory 记忆系统](#memory-记忆系统) |
| 🔌 MCP 与 Browser | 2 | [→ MCP 与 Browser](#mcp-与-browser) |
| 🧩 Skills 相关 | 2 | [→ Skills 相关](#skills-相关) |

---

## 安装与部署

### Q: OpenClaw 支持哪些操作系统？

**A:** OpenClaw 支持 Linux（推荐 Ubuntu 22.04+）、macOS（Intel/Apple Silicon）以及 Windows（通过 WSL2）。生产环境推荐 Linux 部署。

### Q: 安装时提示权限不足怎么办？

**A:** 
```bash
# 方案 1：使用用户级安装
curl -fsSL https://openclaw.dev/install.sh | bash

# 方案 2：检查目录权限
ls -la ~/.openclaw/
chown -R $USER:$USER ~/.openclaw/
```

### Q: 部署后无法连接 Gateway？

**A:** 检查以下几点：
1. 确认 Gateway 端口（默认 3000）未被占用：`lsof -i :3000`
2. 检查防火墙规则：`ufw status`
3. 查看 Gateway 日志：`openclaw logs gateway`

---

## Skills 开发

### Q: 如何创建第一个 Skill？

**A:** 参考 [[03 Skills 插件体系与批量开发]]，最小 Skill 结构：
```
my-skill/
├── SKILL.md    # 技能说明文档
├── _meta.json  # 元数据配置
└── __init__.py # 入口逻辑（可选）
```

### Q: Skill 安装失败，如何排查？

**A:** 
1. 检查 `_meta.json` 格式：`cat _meta.json | python -m json.tool`
2. 检查依赖是否满足：查看 `dependencies` 字段
3. 手动安装测试：`openclaw skill install ./my-skill --verbose`

### Q: Skill 版本冲突如何解决？

**A:** 参考 [[04 Skills 安装与管理实践]]：
```bash
# 查看已安装版本
openclaw skill list --versions

# 强制更新到最新
openclaw skill update <skill-name> --force
```

---

## 自动化与集成

### Q: 定时任务不执行怎么办？

**A:** 参考 [[06 自动化命令与脚本集成]]：
```bash
# 查看任务状态
openclaw cron list

# 查看执行日志
openclaw cron logs <job-id>

# 手动触发测试
openclaw cron run <job-id> --now
```

### Q: 飞书通知发送失败？

**A:** 参考 [[07 飞书集成与消息自动化]]：
1. 确认凭证有效：`openclaw credential list`
2. 检查飞书应用权限（需要 `im:message:create`）
3. 测试连通性：`openclaw message send --channel feishu --target <chat_id> --message "test"`

### Q: 如何配置多个 Agent？

**A:** 参考 [[08 单 Gateway 多 Agent 配置]]，核心配置在 `openclaw.json`:
```json
{
  "agents": {
    "main": { "model": "claude-4-opus", "priority": 1 },
    "assistant": { "model": "claude-4-sonnet", "priority": 2 }
  }
}
```

---

## 故障排查

### Q: 日志在哪里？

**A:** 参考 [[09 故障排查与日志分析]]：
```bash
# 主日志
~/.openclaw/logs/

# 实时查看
openclaw logs -f

# 按级别过滤
openclaw logs --level error
```

### Q: Agent 无响应如何处理？

**A:** 
1. 检查进程状态：`openclaw status`
2. 查看 Agent 日志：`openclaw logs agent`
3. 重启服务：`openclaw restart`
4. 如仍无法解决，参考 [[09 故障排查与日志分析]] 的完整排查流程

---

## 安全与权限

### Q: 如何管理 Credential（凭证）？

**A:** 参考 [[14 安全与权限管理]]：
```bash
# 查看所有凭证
openclaw credential list

# 添加凭证
openclaw credential set <name> <value>

# 删除凭证
openclaw credential remove <name>
```

凭证存储在 `~/.openclaw/credentials/` 目录下，建议通过 `.gitignore` 排除。

### Q: exec-approvals 自动审批如何配置？

**A:** 编辑 `~/.openclaw/exec-approvals.json`，配置允许自动执行的命令模式：
```json
{
  "autoApprove": ["ls", "cat", "echo"],
  "requireApproval": ["rm", "mv", "curl"]
}
```

### Q: 如何进行安全审计？

**A:** 参考 [[14 安全与权限管理]]：
```bash
# 运行内置安全审计
openclaw security audit

# 检查 Skill 安全
openclaw skill vet <skill-name>
```

---

## Memory 记忆系统

### Q: Memory Skill 怎么用？

**A:** 参考 [[15 Memory 记忆系统深入]]：
```bash
# 存储记忆
openclaw memory set "key" "value"

# 检索记忆
openclaw memory get "key"

# 列出所有记忆
openclaw memory list
```

记忆文件存储在 `~/.openclaw/workspace/memory/` 目录下。

### Q: 记忆太多会影响性能吗？

**A:** 会。OpenClaw 采用分类记忆 + 按需加载机制，但超过 500 条仍建议定期归档：
```bash
# 合并相似记忆
openclaw memory merge

# 归档旧记忆
openclaw memory archive --before 30d
```

---

## MCP 与 Browser

### Q: 什么是 MCP？

**A:** MCP (Model Context Protocol) 是 OpenClaw 的工具协议标准。参考 [[16 MCP 工具协议与自定义集成]]，可用 McPorter 管理 MCP Server：
```bash
mcporter list          # 列出已安装 MCP Server
mcporter install <pkg> # 安装新 Server
mcporter status        # 查看运行状态
```

### Q: Browser Relay 如何使用？

**A:** 参考 [[17 浏览器自动化与网页交互]]：
```bash
# 启动 Browser Relay
openclaw browser start

# 导航到页面
openclaw browser navigate "https://example.com"

# 截图
openclaw browser screenshot
```

---

## Skills 相关

### Q: 如何查找和安装新 Skill？

**A:** 
```bash
# 在 ClawdHub 搜索
clawdhub search <keyword>

# 安装 Skill
clawdhub install <skill-slug>

# 或使用 Find Skills 功能
npx skills find <keyword>
```

详见 [[Skills 教程合集]] 获取所有 18 个 Skill 的完整教程。

### Q: Proactive Agent 和 Self-Improving Agent 怎么激活？

**A:** 这两个 Skill 通过 Prompt 注入方式工作，不需要命令调用：
1. **Proactive Agent**: 安装后自动注入到 HEARTBEAT.md，Agent 每次交互时加载
2. **Self-Improving Agent**: 需启用 Hook — `openclaw hooks enable self-improvement`，之后自动在 `.learnings/` 目录下积累经验

---

> 💡 没找到答案？可以在 [GitHub Issues](https://github.com/zxk-git/openclaw-tutorial/issues) 提问。
