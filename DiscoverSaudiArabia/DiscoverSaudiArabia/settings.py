"""
Django settings for DiscoverSaudiArabia project.
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
SECRET_KEY = "django-insecure-_)bu7!u(v^xg!pt+znnsk^ac!_sb37!0up1#6)mxk@1z%iajz)"
DEBUG = True
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "main",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "DiscoverSaudiArabia.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True, 
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "DiscoverSaudiArabia.wsgi.application"


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us" # يمكنك تغييرها إلى "ar" عند الانتهاء
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# 🏆🏆 التعديل النهائي لـ STATICFILES_DIRS 🏆🏆
STATICFILES_DIRS = [
    BASE_DIR / 'static', # إضافة المسار العام (لتغطية أي ملفات خارج مجلد التطبيق)
    BASE_DIR / 'main' / 'static', # المسار الحالي لتطبيق 'main'
]

# لا يزال هذا مطلوبًا لتشغيل collectstatic
STATIC_ROOT = BASE_DIR / 'staticfiles'

# 💥 الإضافة النهائية لكسر الـ Cache بعد كل جمع للملفات 💥
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 🌟🌟🌟 إعدادات البريد الإلكتروني (لصفحة Contact) 🌟🌟🌟
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend' 
RECIPIENT_ADDRESS = 'info@discoversaudi.sa' # هذا يستخدمه views.py
DEFAULT_FROM_EMAIL = 'noreply@discoversaudi.sa'