---
layout: default
title: 随想日志
permalink: /log/
---

<style>
  .log-container {
    max-width: 800px;
    margin: 0 auto;
  }
  
  /* 时间轴外层容器 */
  .log-timeline {
    position: relative;
    padding-left: 20px;
    margin-top: 30px;
    border-left: 2px solid var(--border-color);
  }

  /* 每一条日志项 */
  .log-item {
    position: relative;
    margin-bottom: 35px;
  }

  /* 时间轴上的小圆点 */
  .log-item::before {
    content: "";
    position: absolute;
    left: -26px;
    top: 6px;
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background-color: var(--accent-color);
    border: 2px solid var(--bg-color);
  }

  /* 日志日期 */
  .log-date {
    font-family: var(--font-mono);
    font-size: 0.9rem;
    font-weight: 600;
    color: var(--muted-color);
    margin-bottom: 8px;
  }

  /* 日志正文 */
  .log-content {
    font-size: 1rem;
    line-height: 1.8;
    color: var(--text-color);
  }

  .log-content p {
    margin: 0 0 10px 0;
  }
  .log-content p:last-child {
    margin-bottom: 0;
  }
</style>

<div class="log-container">
  <header class="article-header">
    <h1 class="article-title">随想日志</h1>
    <div class="meta-info">
      记录日常的随感、微语与碎片思考 · 倒序排列
    </div>
  </header>

  <div class="log-timeline">

    <!-- 新日志请加在最上面（倒序排列） -->

    <div class="log-item">
      <div class="log-date">2026-08-14</div>
      <div class="log-content">
        今天建立了日志页面。以后有100~200字的短感想、随笔或读书微语，都可以直接写在这里，无需专门发一篇文章了。
      </div>
    </div>

    <!-- 示例：下一条日志放置在此处 -->

  </div>

  <!-- Utterances 评论区系统 (与关于页面完全相同) -->
  <div class="article-comments" style="margin-top: 4rem; padding-top: 2rem; border-top: 1px solid var(--border-color);">
    <script src="https://utteranc.es/client.js"
            repo="Natural-system/self-transcendence"
            issue-term="pathname"
            theme="github-light"
            crossorigin="anonymous"
            async>
    </script>
  </div>
</div>