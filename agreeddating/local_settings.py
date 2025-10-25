# agreeddating/agreeddating/local_settings.py
# Local development settings - this file should NOT be committed to git

# Development settings
DEBUG = True

# Allow HTTP in development
SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0

# Local hosts
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']

# Use SQLite for local development
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
