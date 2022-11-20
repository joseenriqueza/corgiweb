import os
from pathlib import Path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

INSTALLED_APPS = (
    'corgiweb.data_and_queue.Data.crawler',
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db/corgiweb_db.sqlite3'),
    }
}


SECRET_KEY = '4cCI6MTYzOTQ0NzgwNiwiaWF0IjoxNjM5NDQ3ODA2fQ'