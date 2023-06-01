"""
Django settings for learning_log project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 静态文件URL前缀
STATIC_URL = '../static'
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, '', 'static'),
    os.path.join(BASE_DIR, 'learning_logs', 'static'),
    os.path.join(BASE_DIR, 'learning_log', 'static'),
]
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*$)-a564#9glnva5w!%l(&(s-8y+pwc^7cgnd5f-wnxy$l5=en'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Application definition

INSTALLED_APPS = [
    'simpleui',
    # 'admin_interface',
    # 'colorfield',
    'django.contrib.admin',
    'django.contrib.auth',  # 认证系统使用
    'django.contrib.contenttypes',  # 认证系统使用
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'learning_logs',
    'users',
    # 第三方应用
    'bootstrap3',
    'bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # 认证系统用到
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 认证系统用到
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'learning_log.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'learning_log.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# 配置数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Learning_Log',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 语言改为汉语
LANGUAGE_CODE = 'zh-Hans'
# 时间改为上海时间
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# 我的设置
# 如果未登录的用户访问被装饰器保护的页面，Django将重定向到以下页面
LOGIN_URL = '/users/login/'

SIMPLEUI_LOGO = '/static/img/note.png'
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False
SIMPLEUI_DEFAULT_THEME = 'Highdmin.css'

# django-bootstrap3的设置
BOOTSTRAP3 = {
    'include_jquery': True,
}

# 为了让Django用户认证系统使用我们自定义的用户模型，自定义用户模型所在的位置
AUTH_USER_MODEL = 'users.User'  # 告诉django使用users应用下的User用户模型

# Django会把邮件发送到终端，模拟生产环境下发送邮件
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# EMAIL_HOST = 'smtp.qq.com'  # 发送电子邮箱的SMTP服务器
# EMAIL_PORT = 465  # SMTP服务器端口
# EMAIL_HOST_USER = '13681756546@vip.qq.com'  # 发件人邮箱
# EMAIL_HOST_PASSWORD = 'xxxxxxxx'  # 密码
#
# EMAIL_USE_TLS = False  # 是否使用https（TLS安全传输协议）
# EMAIL_USE_SSL = True  # 是否使用SSL加密
# EMAIL_FROM = 'CorgiNote'  # 发件人

# Heroku设置
# if os.getcwd() == '/app':
#     import dj_database_url
#
#     DEBUG = False
#
#     DATABASES = {
#         'default': dj_database_url.config(default='postgres://localhost')
#     }
#     # 让request.is_secure()承认X-Forwarded-Proto头
#     SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
#
#     # 静态资源配置
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     STATIC_ROOT = 'staticfiles'
#     STATICFILES_DIRS = (os.path.join(BASE_DIR), 'static')