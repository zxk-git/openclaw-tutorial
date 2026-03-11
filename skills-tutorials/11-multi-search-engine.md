<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>

---
[⬅️ 上一篇：Memory](10-memory.md) | [📑 Skills 教程目录](README.md) | [➡️ 下一篇：Notion](12-notion.md)
---

# Multi Search Engine — 17 搜索引擎集成

> **版本**: 2.0.1 | **Slug**: `multi-search-engine` | **难度**: ⭐⭐

---

## 📖 简介

集成 17 个搜索引擎（8 个国内 + 9 个国际），支持高级搜索运算符、时间过滤、站内搜索等，全部无需 API Key，通过 `web_fetch` 直接调用。

---

## 📦 安装

```bash
clawdhub install multi-search-engine
```

**依赖**：仅需 OpenClaw 内置 `web_fetch` 工具。

---

## 🌐 支持的搜索引擎

### 国内引擎（8 个）

| 引擎 | URL 模板 | 特点 |
|------|---------|------|
| 百度 | `https://www.baidu.com/s?wd=关键词` | 中文搜索首选 |
| Bing 中国 | `https://cn.bing.com/search?q=关键词` | 微软搜索 |
| 360 搜索 | `https://www.so.com/s?q=关键词` | 安全搜索 |
| 搜狗 | `https://www.sogou.com/web?query=关键词` | 微信内容搜索 |
| 微信搜索 | `https://weixin.sogou.com/weixin?query=关键词` | 公众号文章 |
| 头条搜索 | `https://so.toutiao.com/search?keyword=关键词` | 今日头条平台 |
| 集思录 | `https://www.jisilu.cn/search/?q=关键词` | 金融投资信息 |
| Bing 国际 | `https://www.bing.com/search?q=keyword` | 英文搜索 |

### 国际引擎（9 个）

| 引擎 | URL 模板 | 特点 |
|------|---------|------|
| Google | `https://www.google.com/search?q=keyword` | 最全面 |
| DuckDuckGo | `https://duckduckgo.com/html/?q=keyword` | 隐私优先 |
| Yahoo | `https://search.yahoo.com/search?p=keyword` | 老牌引擎 |
| Startpage | `https://www.startpage.com/do/search?q=keyword` | 隐私代理 Google |
| Brave | `https://search.brave.com/search?q=keyword` | 独立索引 |
| Ecosia | `https://www.ecosia.org/search?q=keyword` | 环保搜索 |
| Qwant | `https://www.qwant.com/?q=keyword` | 欧洲隐私搜索 |
| WolframAlpha | `https://www.wolframalpha.com/input?i=query` | 知识计算 |
| DuckDuckGo Bangs | `https://duckduckgo.com/html/?q=!bang+keyword` | 快捷跳转 |

---

## 🔧 核心用法

### 基础搜索

```javascript
// Google 搜索
web_fetch({ url: "https://www.google.com/search?q=python+tutorial" })

// 百度搜索
web_fetch({ url: "https://www.baidu.com/s?wd=Python教程" })

// DuckDuckGo
web_fetch({ url: "https://duckduckgo.com/html/?q=OpenClaw+tutorial" })
```

### 高级搜索运算符

```
site:github.com OpenClaw          # 站内搜索
filetype:pdf machine learning     # 文件类型过滤
"exact phrase"                    # 精确匹配
-exclude                          # 排除词
word1 OR word2                    # 或搜索
```

### 时间过滤

```
&tbs=qdr:h    # 过去 1 小时
&tbs=qdr:d    # 过去 1 天
&tbs=qdr:w    # 过去 1 周
&tbs=qdr:m    # 过去 1 月
&tbs=qdr:y    # 过去 1 年
```

### WolframAlpha 知识查询

```javascript
// 汇率换算
web_fetch({ url: "https://www.wolframalpha.com/input?i=100+USD+to+CNY" })

// 数学计算
web_fetch({ url: "https://www.wolframalpha.com/input?i=derivative+of+x^3" })
```

### DuckDuckGo Bangs

```javascript
// !gh → GitHub 搜索
web_fetch({ url: "https://duckduckgo.com/html/?q=!gh+tensorflow" })

// !w → Wikipedia
web_fetch({ url: "https://duckduckgo.com/html/?q=!w+machine+learning" })

// !so → Stack Overflow
web_fetch({ url: "https://duckduckgo.com/html/?q=!so+python+async+await" })
```

---

## 💡 搜索策略建议

| 需求 | 推荐引擎 |
|------|----------|
| 中文内容 | 百度 / Bing 中国 |
| 英文技术 | Google / Brave |
| 微信公众号 | 微信搜索 (搜狗) |
| 隐私搜索 | DuckDuckGo / Startpage |
| 金融数据 | 集思录 |
| 知识计算 | WolframAlpha |
| 新闻时事 | 头条搜索 / Google News |

---

## ❓ 常见问题

**Q: 搜索被限流/验证码？**
切换到其他引擎，或降低请求频率。

**Q: 中文搜索结果乱码？**
确保查询词已正确 URL 编码。

---

<div align="center">

[← Skills 目录](README.md) · [📑 主教程](../README.md)

</div>
