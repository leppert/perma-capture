from .settings_base import *  # noqa

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k2#@_q=1$(__n7#(zax6#46fu)x=3&^lz&bwb8ol-_097k_rj5'

DEBUG = True
CELERY_TASK_ALWAYS_EAGER = True

from celery.schedules import crontab
CELERY_BEAT_SCHEDULE = {
    'demo-scheduled-task': {
        'task': 'main.tasks.demo_scheduled_task',
        'schedule': crontab(minute='*'),
    },
}
CELERY_TASK_ROUTES['main.tasks.demo_scheduled_task'] = {'queue': 'background'}

# don't check password quality locally, since it's annoying
AUTH_PASSWORD_VALIDATORS = []

# django-debug-toolbar:
# ddt can be useful but also be a hassle, so it only runs optionally, if you choose to `pip install django-debug-toolbar`
# If installed, there will be a sidebar when viewing front-end pages, including useful tools such as a SQL profiler.
import sys
if 'pytest' not in sys.modules:  # don't run this from tests
    try:
        import debug_toolbar  # noqa
        if 'debug_toolbar' not in INSTALLED_APPS:
            INSTALLED_APPS += (
                'debug_toolbar',
            )
            MIDDLEWARE.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
            INTERNAL_IPS = ['127.0.0.1']
            DEBUG_TOOLBAR_CONFIG = {
                'SHOW_TOOLBAR_CALLBACK': 'main.utils.show_debug_toolbar'
            }
    except ImportError:
        pass

# Print sent emails to the console, for debugging
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# For testing error reporting
ADMINS = [('John', 'john@example.com'), ('Mary', 'mary@example.com')]

# Minio is available at http://minio:9000 from within this container,
# but is only available at localhost:9000 from the host.
# Override the netloc during serialization, so download links work.
OVERRIDE_DOWNLOAD_URL_NETLOC = 'localhost:9000'


SEND_WEBHOOK_DATA_TO_CAPTURE_SERVICE = True
EXPOSE_WEBHOOK_TEST_ROUTE = True

# Vitejs.dev Setup
VITE_USE_MANIFEST = False
VITE_PORT = '3000'
TEMPLATE_VISIBLE_SETTINGS += ('VITE_PORT',)
