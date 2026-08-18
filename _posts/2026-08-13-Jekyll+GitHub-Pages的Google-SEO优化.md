---
layout: post
title: "Jekyll+GitHub Pages的Google SEO优化"
date: 2026-08-13
categories: 软件
---

对于使用 GitHub Pages 和 Jekyll 搭建的个人静态博客而言，不需要花钱购买营销服务，也不必沉迷于复杂的 SEO 技巧。但**“完全不管”也是不可取的**——若缺乏基础的搜索引擎指引，Google 爬虫检索和收录的速度会非常缓慢，甚至可能误抓一些非必要的页面（如搜索弹窗或 Hash 标签页）。

本文整理了一套**一次性配置、终身受益**的极简 SEO 优化方案。只需 10 到 15 分钟，就能让博客对 Google 搜索引擎大展友好之门。

---

## 一、 生成站点地图（Sitemap）

站点地图（`sitemap.xml`）是给 Google 爬虫提供的“全站地图”，能让爬虫一次性抓取并索引全站的所有文章。

### 配置步骤：

打开项目根目录下的 **`_config.yml`** 文件，在 `plugins` 列表中添加 `jekyll-sitemap` 插件：

```yaml
plugins:
  - jekyll-sitemap
```

> **原理**：提交后，GitHub Pages 在重新构建时会自动在网站根目录下生成一个 `your-domain.com/sitemap.xml` 文件，实时更新全站文章路径。

## 二、 补全 `<head>` 基础 SEO 与 Open Graph 元数据

在 HTML 的 `<head>` 头部补充标准的 Description（描述）、Canonical（规范网址）以及 Open Graph 标签，能够让 Google 搜索结果呈现清晰的网页摘要，同时也改善了微信、Twitter、Telegram 等社交平台分享时的卡片显示效果。

### 配置步骤：

打开你的布局文件（如 `_layouts/default.html`），在 `<head>` 标签内部补充以下标准代码：

{% raw %}

HTML

```
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% if page.title %}{{ page.title }} - {{ site.title }}{% else %}{{ site.title }}{% endif %}</title>
  
  <!-- SEO 描述与关键词 -->
  <meta name="description" content="{{ page.excerpt | strip_html | strip_newlines | truncate: 150 | default: site.description }}">
  
  <!-- Open Graph 标签（社交平台分享卡片） -->
  <meta property="og:title" content="{% if page.title %}{{ page.title }} - {{ site.title }}{% else %}{{ site.title }}{% endif %}">
  <meta property="og:description" content="{{ page.excerpt | strip_html | strip_newlines | truncate: 150 | default: site.description }}">
  <meta property="og:type" content="{% if page.title %}article{% else %}website{% endif %}">
  <meta property="og:url" content="{{ page.url | absolute_url }}">

  <!-- 规范链接（防止重复内容导致搜索引擎权重分散） -->
  <link rel="canonical" href="{{ page.url | absolute_url }}">
</head>
```

{% endraw %}

## 三、 创建 `robots.txt` 爬虫指引文件

`robots.txt` 用于明确告诉搜索引擎哪些页面可以抓取，并指明站点地图的具体位置。

### 配置步骤：

在项目的 **根目录** 下新建一个名为 **`robots.txt`** 的文件，写入以下内容（注意替换为你的真实域名）：

Plaintext

````
```text
User-agent: *
Allow: /

Sitemap: [https://your-domain.com/sitemap.xml](https://your-domain.com/sitemap.xml)
```
````

## 四、 主动向 Google Search Console 提交站点

若只被动等待爬虫收录，新站点可能需要数周甚至数月。通过控制台主动提交站点地图，通常可以在 **24~48 小时** 内完成首批页面的检索与收录。

### 操作流程：

1. 访问 [Google Search Console](https://search.google.com/search-console) 并使用 Google 账号登录。
2. 选择 **网址前缀（URL prefix）**，输入你的博客网址（如 `https://xxx.github.io` 或独立域名）。
3. **验证所有权**：下载 Google 提供的 HTML 验证文件，放置在博客根目录，提交推送成功后点击“验证”。
4. **提交 Sitemap**：验证通过后，在左侧菜单栏进入 **站点地图（Sitemaps）**，输入 `sitemap.xml` 并点击提交。

## 总结

完成上述四步后，无需再为 SEO 耗费额外精力。

Jekyll 生成的纯静态 HTML 网页结构优雅、无阻碍加载的垃圾脚本、访问响应迅速，天然契合搜索引擎的偏好。今后只需专注于 Markdown 文章的创作，GitHub Pages 每次部署均会自动更新站点地图并完成收录巡检。

*本文使用谷歌 AI 生成*