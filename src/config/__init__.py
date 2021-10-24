#!/usr/bin/env python
import os

import packs

import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()

'''Rename tables in database'''
packs.rename_tables()
