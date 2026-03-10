---
[⬅️ 上一篇：GitHub](07-github.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Markdown Converter](09-markdown-converter.md)
---

# GoG — Google Workspace CLI

> **版本**: 1.0.0 | **Slug**: `gog` | **难度**: ⭐⭐⭐

---

## 📖 简介

Google Workspace 命令行工具，支持 Gmail、Calendar、Drive、Contacts、Sheets、Docs 全套操作。

---

## 📦 安装

```bash
clawdhub install gog
```

---

## ⚙️ 首次配置

### 1. 获取 OAuth 客户端凭据

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建项目，启用所需 API（Gmail、Calendar、Drive、Sheets 等）
3. 创建 OAuth 2.0 凭据，下载 `client_secret.json`

### 2. 配置认证

```bash
gog auth credentials /path/to/client_secret.json
```

### 3. 设置默认账户

```bash
export GOG_ACCOUNT=you@gmail.com
```

---

## 🔧 核心用法

### Gmail

```bash
# 搜索近 7 天邮件
gog gmail search 'newer_than:7d' --max 10

# 搜索特定发件人
gog gmail search 'from:boss@company.com' --max 5

# 发送邮件
gog gmail send --to "user@example.com" --subject "Hello" --body "Content"
```

### Calendar

```bash
# 查看日程
gog calendar events <calendarId> --from 2026-03-10T00:00:00Z --to 2026-03-17T00:00:00Z

# 创建事件
gog calendar create <calendarId> --title "Meeting" --start "2026-03-11T10:00" --end "2026-03-11T11:00"
```

### Sheets

```bash
# 读取数据
gog sheets get <sheetId> "Sheet1!A1:D10" --json

# 更新单元格
gog sheets update <sheetId> "Sheet1!A1" --values-json '[["New Value"]]'

# 追加数据
gog sheets append <sheetId> "Sheet1!A:D" --values-json '[["Col1","Col2","Col3","Col4"]]'

# 清空区域
gog sheets clear <sheetId> "Sheet1!A1:D10"
```

### Drive

```bash
# 搜索文件
gog drive search "quarterly report" --max 10
```

### Docs

```bash
# 导出文档内容
gog docs export <docId>
```

---

## 💡 使用技巧

- 设置 `GOG_ACCOUNT` 环境变量避免每次指定账号
- 使用 `--json` 获取 JSON 格式输出
- Sheets 操作的 `--values-json` 接受嵌套数组格式

---

## ❓ 常见问题

**Q: 认证过期？**
重新运行 `gog auth credentials /path/to/client_secret.json`。

**Q: 权限不足？**
确认 Google Cloud Console 中已启用对应 API。

---

> 📖 [返回 Skills 教程目录](README.md)
