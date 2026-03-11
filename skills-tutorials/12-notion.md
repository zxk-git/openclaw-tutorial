<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>

---
[⬅️ 上一篇：Multi Search Engine](11-multi-search-engine.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：PowerPoint PPTX](13-powerpoint-pptx.md)
---

# Notion — Notion API 集成

> **版本**: 1.0.0 | **Slug**: `notion` | **难度**: ⭐⭐

---

## 📖 简介

通过 Notion API 创建和管理页面、数据库和内容块。使用最新 API 版本 2025-09-03。

---

## 📦 安装

```bash
clawdhub install notion
```

---

## ⚙️ 首次配置

### 1. 创建 Notion Integration

1. 访问 https://notion.so/my-integrations
2. 点击 "New integration"
3. 命名（如 "OpenClaw"），选择关联的 workspace
4. 复制 API Key（`ntn_` 开头）

### 2. 存储 API Key

```bash
mkdir -p ~/.config/notion
echo "ntn_your_api_key_here" > ~/.config/notion/api_key
chmod 600 ~/.config/notion/api_key
```

### 3. 共享页面给 Integration

在 Notion 中，进入你想要操作的页面/数据库：
1. 点击右上角 `...` → `Connections`
2. 添加你创建的 Integration

> **重要**：Integration 只能访问明确共享给它的页面。

---

## 🔧 核心用法

### 搜索

```bash
curl -X POST 'https://api.notion.com/v1/search' \
  -H 'Authorization: Bearer ntn_xxx' \
  -H 'Notion-Version: 2025-09-03' \
  -H 'Content-Type: application/json' \
  -d '{"query": "项目文档"}'
```

### 读取页面

```bash
curl 'https://api.notion.com/v1/pages/<page-id>' \
  -H 'Authorization: Bearer ntn_xxx' \
  -H 'Notion-Version: 2025-09-03'
```

### 创建页面

```bash
curl -X POST 'https://api.notion.com/v1/pages' \
  -H 'Authorization: Bearer ntn_xxx' \
  -H 'Notion-Version: 2025-09-03' \
  -H 'Content-Type: application/json' \
  -d '{
    "parent": {"page_id": "parent-page-id"},
    "properties": {
      "title": [{"text": {"content": "New Page Title"}}]
    }
  }'
```

### 查询数据库

```bash
curl -X POST 'https://api.notion.com/v1/databases/<db-id>/query' \
  -H 'Authorization: Bearer ntn_xxx' \
  -H 'Notion-Version: 2025-09-03' \
  -H 'Content-Type: application/json' \
  -d '{"filter": {"property": "Status", "select": {"equals": "Done"}}}'
```

### 创建数据库条目

```bash
curl -X POST 'https://api.notion.com/v1/pages' \
  -H 'Authorization: Bearer ntn_xxx' \
  -H 'Notion-Version: 2025-09-03' \
  -H 'Content-Type: application/json' \
  -d '{
    "parent": {"database_id": "db-id"},
    "properties": {
      "Name": {"title": [{"text": {"content": "New Item"}}]},
      "Status": {"select": {"name": "In Progress"}}
    }
  }'
```

---

## 💡 使用场景

| 场景 | 操作 |
|------|------|
| 知识库管理 | 搜索 + 读取页面内容 |
| 任务追踪 | 查询/更新数据库条目 |
| 文档创建 | 创建页面 + 添加内容块 |
| 数据同步 | 批量读取数据库 → 本地处理 |

---

## ❓ 常见问题

**Q: 报 401 错误？**
检查 API Key 是否正确，页面是否已共享给 Integration。

**Q: 搜索不到页面？**
确认页面已通过 Connections 共享给你的 Integration。

---

<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>
