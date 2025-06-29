from pathlib import Path
from decouple import config
import os

# BASE DIR
BASE_DIR = Path(__file__).resolve().parent.parent

# SEGURANÇA
SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# APLICAÇÕES
INSTALLED_APPS = [
	# Django apps
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',

	# Apps locais
	'pacientes',
]

# MIDDLEWARE
MIDDLEWARE = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CONFIGURAÇÃO DE URLS
ROOT_URLCONF = 'projeto_health.urls'

# TEMPLATE
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [BASE_DIR / 'templates'],
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

# WSGI
WSGI_APPLICATION = 'projeto_health.wsgi.application'

# BANCO DE DADOS
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': BASE_DIR / 'db.sqlite3',
	}
}

# VALIDAÇÃO DE SENHAS
AUTH_PASSWORD_VALIDATORS = [
	{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
	{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
	{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
	{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# LOCALIZAÇÃO
LANGUAGE_CODE = 'pt-MZ'
TIME_ZONE = 'Africa/Maputo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# CAMPOS AUTOMÁTICOS
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# E-MAIL (console ou SMTP)
EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')

# ARQUIVOS ESTÁTICOS
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ARQUIVOS DE MÍDIA
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# AUTENTICAÇÃO
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'

# SESSÃO
SESSION_COOKIE_AGE = 1800  # 30 minutos
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SAVE_EVERY_REQUEST = True
