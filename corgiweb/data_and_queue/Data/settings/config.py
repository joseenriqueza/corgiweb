import os

from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'corgiweb.data_and_queue.Data.settings.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "corgiweb.data_and_queue.Data.settings.settings")

application = get_wsgi_application()
