# Self-Transcendence 个人极简纯文字博客 · 技术主题实现

这个开源项目是基于 Jekyll 构建。聚焦 **主题可视化切换**、**双轨内容架构**、**阅读进度追踪** 与 **轻量级数据懒加载**。
*Self-Transcendence，当然这个名字大家可以自行更改，这只是我个人用于写我博客而设的一个名字，仅此而已。
---

## 🌟 核心技术特性一览

### 1. 🎨 **四色主题自由切换** —— 基于 CSS 变量体系的无闪技术方案

**技术实现**：通过 `localStorage` + `document.documentElement.setAttribute('data-theme', targetTheme)` 实现零闪动切换。

- 所有颜色变量（背景色、文字色、边框色、强调色）集中托管于 `:root` 与 `html[data-theme]` 伪类，**切换过程无需重绘整个 DOM**，仅改变 CSS 变量值。
- 主题切换器的 `.theme-dot` 圆形按钮采用 `active` 类高亮当前模式，状态持久化保存在浏览器本地。
- **四种主题**：
  - **日光**（默认）：白底黑字，高对比度。
  - **羊皮纸**：暖黄底色，复古阅读感。
  - **护眼绿**：低饱和度绿色背景，减轻视觉疲劳。
  - **暗黑**：深灰底色，适合夜间或弱光环境。

> 该主题体系与页面上的 **代码块配色** 联动，暗黑模式下的代码块背景自动适配为深色，全文保持视觉一致性。

---

### 2. 🧠 **双轨内容架构** —— `_posts` 与 `_logs` 分离设计

传统个人博客仅有一种内容类型。本项目的核心设计理念是 **“正式文章”与“碎片随感”分轨管理**，其技术实现如下：

| 内容类型 | 目录       | 渲染布局 | 核心交互技术 |
| -------- | ---------- | -------- | ------------ |
| **文章** | `_posts/`  | `post.html` | 自动生成侧边栏 TOC 目录（扫描 h2/h3 标题并赋予 id） |
| **日志** | `_logs/`   | `log.html`  | 时间线分组（年/月/日）+ 滚动触底懒加载（`IntersectionObserver` API） |

**技术亮点**：
- **日志懒加载机制**：首次仅渲染 `BATCH_SIZE = 50` 条日志，滚动至底部触发点后，由 `IntersectionObserver` 监测到并分批加载剩余条目，**显著降低首屏加载压力**，适合日志体量较大的长期写作。
- **时间线侧栏导航**：自动解析日志的年/月/日层级结构，生成 **折叠树状菜单**，点击任意日期可 `scrollIntoView` 并附带高亮动画（CSS `@keyframes highlightFade`）。

---

### 3. 📊 **阅读进度条 + 文章目录联动** —— 极简交互的细节注入

**进度条**：固定于页面顶部的 `<div class="progress-bar">` 通过监听 `window.onscroll` 事件实时计算已读百分比，宽度随滚动动态更新。

**文章目录 (TOC)**：
- 在 `post.html` 中利用 JavaScript 扫描 `.js-article-body` 下的所有 `h2` 与 `h3` 元素，自动生成嵌套无序列表。
- 若标题未手动设置 `id`，脚本会以 `toc-heading-{index}` 格式自动补全，确保锚点跳转正常。
- 目录悬浮于侧边栏，随页面滚动保持固定 (`position: sticky`)，并具备 **悬停右移 4px** 的微交互效果。

---

### 4. 🔍 **全站全文搜索** —— 基于 Jekyll 构建时的数据预埋

**技术思路**：在 Jekyll 构建阶段，将 `site.posts` 中的所有文章标题、URL、发布日期、正文内容序列化为一个 **全局 JavaScript 数组** `globalSearchDB`，由 `default.html` 内联注入。

- 搜索框位于顶部导航栏，**输入即触发** (`oninput`)，无需点击按钮。
- 匹配逻辑：同时检索 `title` 与 `content` 字段，符合条件的结果以 **模态弹窗** 形式展示，且支持 `ESC` 键关闭。
- 这种 **“构建时索引 + 运行时检索”** 模式，无需依赖任何第三方搜索引擎，**完全脱机可用**，且响应迅速。

---

### 5. 🧩 **代码块一键复制** —— 提升技术写作的阅读体验

- 每个 `<pre>` 代码块在页面加载完成后，由 JavaScript 动态注入 `.copy-code-button` 按钮。
- 使用 `navigator.clipboard.writeText` API 实现复制，并提供“已复制!”的 2 秒状态反馈。
- 按钮仅在鼠标悬停时显现 (`opacity: 0.6 → 1`)，**避免干扰阅读视线**。

---

### 6. 📆 **智能分页与年份折叠归档** —— 纯 CSS 折叠方案

- **首页与分类页**：均采用 **JS 驱动分页**，并附带 **页码跳转输入框**，支持直接输入页码跳转。
- **年份归档页**：采用 **纯 CSS 折叠技术**（`<input type="checkbox">` + 兄弟选择器 `~`），无需 JavaScript 即可展开/收起超过 10 篇的年份文章列表。
- 同时利用 `nth-child(9)` 与 `nth-child(10)` 选择器，在默认收起状态下为第 9、10 篇文章施加 **透明度递减渐变**，视觉上提示“更多内容可展开”。

---

## 🗂️ 项目目录结构

```bash
.
├── _posts/                 # 正式文章 (支持分类、TOC)
├── _logs/                  # 日常日志 (按 year 字段分组)
├── _layouts/               # 页面布局模板
│   ├── default.html        # 全局主布局 (导航、主题切换、搜索)
│   ├── post.html           # 文章页 (侧边栏 TOC + Utterances 评论)
│   ├── log.html            # 日志页 (时间线 + 懒加载 + 树状侧栏)
│   ├── page.html           # 独立页面 (about 等)
│   └── archive.html        # 年份归档 (纯 CSS 折叠展开)
├── _includes/              # 可复用组件 (toc.html 目录生成器)
├── assets/                 # 样式资源
├── index.html              # 首页 (文章列表 + 分页)
├── categories.html         # 分类归档 (分类聚合 + 分页)
├── archive.html            # 年份归档
├── about.md                # 关于页面
├── _config.yml             # Jekyll 配置
└── README.md               # 本文件
```

---

## 🚀 快速开始 (本地开发)

确保已安装 Ruby 和 Bundler：

```bash
git clone https://github.com/Natural-system/self-transcendence.git
cd self-transcendence
bundle install
bundle exec jekyll serve
# 访问 http://localhost:4000
```

---

## 📄 开源协议

本项目采用 **MIT License**，欢迎 Fork、二次开发与使用。

**如果你喜欢这个博客体系的设计理念，请点亮 Star ⭐ 支持一下！**
