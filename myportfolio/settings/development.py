# # development.py
# # from .base import *

# import os

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-xqdxj4)wa_d55$$!x&tr*f)j1iz@t9c1jf@vnd$&hkpw1a8100'

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = [] #['localhost', '127.0.0.1']

# # Database
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.2/howto/static-files/
# STATIC_URL = '/static/'
# STATICFILES_DIRS = [BASE_DIR / 'static',]

# # Media Files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = BASE_DIR / 'media'

# # Email Backend
# # During development, console backend prints emails to the console
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# # Logging
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'console': {
#             'class': 'logging.StreamHandler',
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console'],
#             'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
#         },
#     },
# }

# # Django Debug Toolbar (optional)
# # To use Django Debug Toolbar, you'd need to install it first using pip
# # and then include it in your INSTALLED_APPS and MIDDLEWARE.
# if DEBUG:
#     INSTALLED_APPS += [
#         'debug_toolbar',
#     ]
#     MIDDLEWARE += [
#         'debug_toolbar.middleware.DebugToolbarMiddleware',
#     ]
#     INTERNAL_IPS = ['127.0.0.1',]

# # Add any development-specific apps or middleware here

