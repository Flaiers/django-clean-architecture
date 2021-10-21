import os

from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).parent.parent.parent.parent

# reading ./deployment/.env file
load_dotenv(os.path.join(BASE_DIR, 'deployment', '.env'))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}
