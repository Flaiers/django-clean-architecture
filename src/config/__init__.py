#!/usr/bin/env python
import os

import django

from packs import rename_tables


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

'''Rename tables in database'''
rename_tables()
