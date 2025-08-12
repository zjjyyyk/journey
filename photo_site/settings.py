import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'replace-me-in-production'
# DEBUG = True
DEBUG = False  # 生产环境建议设置为 False
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.staticfiles',
    'gallery',
    'django_distill',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
]

ROOT_URLCONF = 'photo_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'photo_site.wsgi.application'

# 无数据库配置，项目只从文件系统读取图片
DATABASES = {}

# 静态文件配置
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']  # 开发时的静态文件目录
STATIC_ROOT = BASE_DIR / 'static_root'    # collectstatic 收集目标目录，django-distill 会检测此目录
STATICFILES_STORAGE = 'gallery.storage.RelativeStaticFilesStorage'

# 媒体文件配置（你的照片）
MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = 'media/'

# 方便调试，开发时允许 Django 提供媒体文件

