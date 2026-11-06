---
permalink: /
title: ""
excerpt: ""
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

{% if site.google_scholar_stats_use_cdn %}
{% assign gsDataBaseUrl = "https://cdn.jsdelivr.net/gh/" | append: site.repository | append: "@" %}
{% else %}
{% assign gsDataBaseUrl = "https://raw.githubusercontent.com/" | append: site.repository | append: "/" %}
{% endif %}
{% assign url = gsDataBaseUrl | append: "google-scholar-stats/gs_data_shieldsio.json" %}

<span class='anchor' id='about-me'></span>

Hi! I am a Computer Science PhD candidate at the University of Liverpool, supervised by [Dr. Rui Yang](https://scholar.xjtlu.edu.cn/en/persons/RYang/). I am nearing completion of my PhD and currently seeking postdoctoral opportunities.

My research focuses on EEG data, foundation models, neural data processing, and transfer learning. If you have a suitable opportunity or would like to collaborate, please feel free to contact me at [Chengxuan.Qin@outlook.com](mailto:Chengxuan.Qin@outlook.com).

# 🔥 News
- *2026-11*: [EEG-Arena](https://www.modelscope.cn/datasets/orangeeg/eeg-arena), our standardized downstream-task benchmark collection, is now available on ModelScope. We welcome the community to download and use it.
- *2026-09*: Our paper, “[Benchmarking EEG Foundation Models at Scale: Lessons from 20,000 Evaluations](https://arxiv.org/abs/2609.32743),” was accepted to the NeurIPS 2026 Evaluations & Datasets Track.
- *2026-09*: Our neural data infrastructure portal, [EEG.FM](https://eeg.fm/), is now live. We invite the community to explore and use it.
- *2025-11*: Our paper, “[EEG-Infinity: A Mathematical Modeling-Inspired Architecture for Addressing Cross-Device Challenges in Motor Imagery](https://doi.org/10.1109/TNSRE.2025.3635018),” was accepted for publication in *IEEE Transactions on Neural Systems and Rehabilitation Engineering*.
- *2025-11*: Our team, [MIN~C² (MIND-CICO)](https://eeg2025.github.io/leaderboard/), placed third in both Challenge 1 and Challenge 2 of the NeurIPS 2025 EEG Challenge.
- *2025-04*: Our paper, “[EEGUnity: Open-Source Tool in Facilitating Unified EEG Datasets Toward Large-Scale EEG Model](https://doi.org/10.1109/TNSRE.2025.3565158),” was accepted for publication in *IEEE Transactions on Neural Systems and Rehabilitation Engineering*.
- *2023-09*: A paper was accepted for publication in *IEEE Transactions on Neural Systems and Rehabilitation Engineering*.
- *2023*: A paper was submitted to *IEEE Transactions on Neural Systems and Rehabilitation Engineering*.

# 📝 Publications

{% include publications.html %}

# 📖 Education
- *Dec 2023–Jun 2027 (expected)*: PhD in Computer Science, University of Liverpool
- *Sep 2021–Apr 2023*: Master of Research in Pattern Recognition and Intelligent Systems, University of Liverpool
- *Sep 2017–Jun 2021*: Bachelor of Engineering in Robot Engineering, Guangzhou University

# 💻 Experience
- *Feb 2026–Present*: Research Assistant, Xi’an Jiaotong-Liverpool University. Developing an LLM-powered intelligent assistant for the Nexteer project to improve access to project knowledge and support engineering workflows.
- *Jan 2022–Dec 2026*: Teaching Assistant, Xi’an Jiaotong-Liverpool University. Supported INT411, INT301, INT201, RBT101, and RBT201, covering machine learning, robotics, and reinforcement learning.
