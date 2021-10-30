from dotenv import load_dotenv

from pathlib import Path

import os

BASE_DIR = Path(__file__).parent.parent.parent.parent

# reading ./deployment/example.env file
load_dotenv(os.path.join(BASE_DIR, 'deployment', 'example.env'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
