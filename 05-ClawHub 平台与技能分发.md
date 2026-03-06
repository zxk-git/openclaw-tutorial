# 第5章：ClawHub 平台与技能分发

> 本章介绍 ClawHub（又名 skills.sh）技能市场平台，包括如何浏览、安装、发布技能，以及社区协作流程。

---

## 5.1 ClawHub 平台简介

ClawHub（访问地址 https://skills.sh）是 OpenClaw 的官方技能市场，提供经过审核的 Skills 供用户搜索和安装。

### 核心功能

- 浏览和搜索可用 Skills
- 一键安装到本地
- 技能评分与评论
- 开发者发布与版本管理
- 社区贡献与协作

### 使用方式

```bash
# 从 ClawHub 安装
clawdhub install <skill-name>

# 搜索可用技能
npx skills find "关键词"
```

---

## 5.2 浏览与搜索技能

### 在线浏览

访问 https://skills.sh 可按分类浏览所有可用 Skills。

### 命令行搜索

```bash
# 按关键词搜索
npx skills find "search"
npx skills find "automation"

# 查看技能详情
npx skills info tavily-search
```

### 常见分类

| 分类 | 说明 | 推荐技能 |
|------|------|---------|
| 搜索 | 网络搜索引擎集成 | tavily-search, ddg-web-search |
| 办公 | 办公软件集成 | gog, notion |
| 开发 | 开发工具 | github, file-search |
| AI | Agent 增强 | proactive-agent, memory |
| 安全 | 安全审查 | skill-vetter |

---

## 5.3 发布技能到 ClawHub

开发完成的 Skill 可以发布到 ClawHub 供社区使用。

### 发布前检查

1. SKILL.md 格式正确（frontmatter 完整）
2. 包含必要的 README.md
3. 脚本可独立运行
4. 声明所有依赖
5. 通过 skill-vetter 安全审查

### 发布流程

```bash
# 初始化发布配置
npx skills init

# 验证 Skill 格式
npx skills validate

# 发布
npx skills publish
```

### 版本更新

```bash
# 更新版本号（在 SKILL.md 中修改 version）
# 重新发布
npx skills publish
```

---

## 5.4 社区协作

ClawHub 鼓励社区贡献与协作。

### 贡献方式

- **报告问题**：在 Skill 的 GitHub 仓库提交 Issue
- **提交改进**：Fork → 修改 → Pull Request
- **分享经验**：编写使用教程和最佳实践
- **评分评论**：在 ClawHub 对使用过的 Skill 评分

### 开发协作

```bash
# Fork 他人的 Skill
git clone https://github.com/author/skill-name.git
cd skill-name

# 修改并测试
# 提交 Pull Request
git push origin feature-branch
```

---

## 常见问题

| 问题 | 解决方法 |
|------|---------|
| 如何注册 ClawHub 账号 | 访问 https://skills.sh 使用 GitHub 账号登录 |
| 发布的 Skill 如何审核 | ClawHub 团队会对公开发布的 Skill 进行自动化安全扫描和人工审核 |
| Skill 被拒绝发布怎么办 | 查看拒绝原因，通常是安全问题或格式不符，修复后重新提交 |

---

## 本章小结

- ClawHub 平台与技能分发 是 OpenClaw 平台的重要功能。
- ClawHub 平台简介：掌握其核心概念和操作方法。
- 浏览与搜索技能：掌握其核心概念和操作方法。
- 发布技能到 ClawHub：掌握其核心概念和操作方法。
- 社区协作：掌握其核心概念和操作方法。
- 遇到问题时，善用 `openclaw doctor` 进行诊断。

> 下一章：自动化命令与脚本集成
