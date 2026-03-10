---
[⬅️ 上一篇：Find Skills](06-find-skills.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：GoG](08-gog.md)
---

# GitHub — gh CLI 集成

> **版本**: 1.0.0 | **Slug**: `github` | **难度**: ⭐⭐

---

## 📖 简介

通过 `gh` CLI 与 GitHub 交互，支持 Issues、Pull Requests、CI 运行查看和高级 API 查询。所有命令支持 `--json` 结构化输出。

---

## 📦 安装

```bash
clawdhub install github
```

### 前置依赖

需要先安装 `gh` CLI：

```bash
# Debian/Ubuntu
apt install gh

# macOS
brew install gh

# 认证
gh auth login
```

---

## 🔧 核心用法

### PR 管理

```bash
# 查看 PR 的 CI 状态
gh pr checks 55 --repo owner/repo

# 查看 PR 详情
gh pr view 55 --repo owner/repo

# 列出所有 PR
gh pr list --repo owner/repo --json number,title,state

# 创建 PR
gh pr create --title "feat: ..." --body "..." --base main
```

### Issue 管理

```bash
# 列出 Issues（JSON 格式）
gh issue list --repo owner/repo --json number,title,labels

# 创建 Issue
gh issue create --title "Bug: ..." --body "..."

# 按标签过滤
gh issue list --label "bug" --repo owner/repo
```

### CI/CD 运行

```bash
# 查看 Workflow 运行列表
gh run list --repo owner/repo

# 查看失败日志
gh run view <run-id> --repo owner/repo --log-failed

# 重新运行失败的 Workflow
gh run rerun <run-id> --repo owner/repo
```

### 高级 API 查询

```bash
# 使用 gh api + jq 过滤
gh api repos/owner/repo/pulls/55 --jq '.title'

# 获取仓库信息
gh api repos/owner/repo --jq '{stars: .stargazers_count, forks: .forks_count}'
```

---

## 💡 最佳实践

- 所有命令加 `--json` 获取结构化输出，方便程序处理
- 使用 `--jq` 在命令行直接过滤 JSON 结果
- CI 排查失败时用 `--log-failed` 只看失败部分，避免信息过载

---

## ❓ 常见问题

**Q: gh auth 失败？**
确保可以访问 GitHub，运行 `gh auth login` 选择合适的认证方式。

**Q: 没有权限操作某个仓库？**
检查 Token 作用域，运行 `gh auth refresh -s repo` 扩展权限。

---

> 📖 [返回 Skills 教程目录](README.md)
