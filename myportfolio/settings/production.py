# # production.py
# # from .base import *

# import os
# import dj_database_url
# from django.core.exceptions import ImproperlyConfigured

# def get_env_variable(var_name):
#     """Get the environment variable or return exception."""
#     try:
#         return os.environ[var_name]
#     except KeyError:
#         error_msg = f"Set the {var_name} environment variable."
#         raise ImproperlyConfigured(error_msg)

# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-default-secret-key')

# # SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True #False

# # ALLOWED_HOSTS = ['yourwebsite.com', 'www.yourwebsite.com']
# ALLOWED_HOSTS = []

# # Database
# # Use dj_database_url to parse the DATABASE_URL environment variable
# DATABASES = {
#     'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
# }

# # Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # Media Files
# MEDIA_URL = '/media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # Security settings
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_SECURE = True
# CSRF_COOKIE_SECURE = True
# SECURE_BROWSER_XSS_FILTER = True
# SECURE_CONTENT_TYPE_NOSNIFF = True
# X_FRAME_OPTIONS = 'DENY'

# # Email configuration
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.yourmailprovider.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', 'your-email@example.com')
# EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')

# # Logging
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'handlers': {
#         'file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': os.path.join(BASE_DIR, 'logs/django_errors.log'),
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['file'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#     },
# }

# # Additional middleware for security
# MIDDLEWARE += [
#     'django.middleware.security.SecurityMiddleware',
# ]

# # Add any production-specific apps
# INSTALLED_APPS += [
#     # Example: 'django_minify_html.middleware.MinifyHtmlMiddleware',
# ]

# # Ensure you replace 'yourwebsite.com' with your actual domain name,
# # update the EMAIL_* settings to match your email service provider's settings,
# # and make sure all environment variables are set in your production environment.
