from dotenv import load_dotenv

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# reading ./deployment/example.env file
load_dotenv(os.path.join(BASE_DIR, 'deployment', 'example.env'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
