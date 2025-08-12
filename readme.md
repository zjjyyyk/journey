# Photo Gallery - 静态相册生成器

这是一个基于 Django 的静态网站生成器，旨在将您按文件夹组织的本地照片，快速转换成一个精美、可部署的在线相册网站。

## ✨ 主要特性

-   **目录即相册**: 自动将 `media` 文件夹下的两级目录结构 (`时间/地点人物`) 识别为相册。
-   **自动缩略图**: 内置脚本一键为所有照片生成高清缩略图，优化加载速度。
-   **纯静态输出**: 使用 `django-distill` 生成纯粹的 HTML/CSS 静态网站，可部署在任何地方。
-   **子目录部署**: 已完全配置为支持部署到网站的子目录 (例如 `your-domain.com/journey`)，完美适配 GitHub Pages。
-   **简约设计**: 界面简洁、响应式，您可以轻松通过修改 CSS 来自定义风格。
-   **无需数据库**: 完全基于文件系统，无需配置和维护数据库。

## 🚀 快速开始

### 1. 环境准备

确保您的电脑上已安装：
-   Python 3.10 或更高版本
-   Git

### 2. 获取项目

克隆此仓库到您的本地：
```bash
git clone https://github.com/zjjyyyk/journey.git
cd journey
```

### 3. 安装依赖

项目依赖已在 `requirements.txt` 中列出。建议使用虚拟环境：

```bash
# 创建并激活虚拟环境 (macOS/Linux)
python3 -m venv venv
source venv/bin/activate

# (Windows)
# python -m venv venv
# venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 4. 放入照片

将您的照片放入 `media` 文件夹，并遵循以下两级目录结构：

```
media/
└── 2025_Summer/
    ├── Paris_Alice/
    │   ├── photo1.jpg
    │   └── photo2.png
    └── London_Bob/
        └── photo3.jpg
```
> **提示**: 第一级目录（如 `2025_Summer`）会被视作一个“时期”，第二级目录（如 `Paris_Alice`）会被作为该时期下的一个分组。

### 5. 生成缩略图

运行脚本为所有照片创建缩略图。脚本会自动跳过已存在的缩略图。

```bash
python generate_thumbs.py
```

### 6. 本地预览

本地预览时，首先注释掉`templates/base.html` 中已设置的 `<base href="/journey/">` 标签，这个标签是为了部署到子目录而设置的相对路径。

启动 Django 开发服务器，在本地浏览器中预览效果：

```bash
python manage.py runserver
```
然后访问 `http://127.0.0.1:8000`。

### 7. 生成静态网站

当您对预览效果满意后，运行以下命令生成最终的静态网站文件。所有文件将被输出到 `output` 文件夹中。

```bash
python manage.py distill-local output --force
```

## 部署

生成的静态网站可以被部署在任何静态托管服务上，例如 GitHub Pages, Netlify, Vercel 等。

本项目已为部署到 GitHub Pages 的子目录（例如 `https://<Your-Username>.github.io/journey/`）做好了预配置：

-   所有生成的 URL 均为相对路径。
-   `templates/base.html` 中已设置 `<base href="/journey/">` 标签。如果您注释了该标签，需要取消注释。
-   `.github/workflows/deploy.yml` 文件提供了一个开箱即用的 GitHub Actions 工作流，它会在您推送到 `main` 分支时自动构建和部署网站到 `gh-pages` 分支。

您只需根据您的仓库名，适当修改 `templates/base.html` 中的 `/journey/` 路径即可。

## 🎨 自定义

-   **样式**: 网站的所有样式都在 `static/css/site.css` 文件中，您可以直接修改它来改变网站外观。
-   **模板**: 如果您想调整页面布局和 HTML 结构，可以修改 `templates/` 目录下的模板文件。