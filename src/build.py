#!/usr/bin/env python
import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

django.setup()


def main():
    from django.contrib.auth import get_user_model

    '''Create first superuser'''
    UserModel = get_user_model()
    User = UserModel.objects.filter(username='root')
    if User.exists():
        print('Root user already exists!')
    else:
        UserModel.objects.create_superuser(
            username='root',
            password='root',
            email='root@root.com'
        )
        print('Root user created!')


if __name__ == '__main__':
    main()
