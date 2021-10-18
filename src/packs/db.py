def rename_tables() -> None:
    
    from django.db.migrations.recorder import MigrationRecorder
    from django.contrib.contenttypes.models import ContentType
    from django.contrib.auth.models import User, Group, Permission
    from django.contrib.sessions.models import Session
    from django.contrib.admin.models import LogEntry


    MigrationRecorder.Migration()

    User._meta.db_table = 'users'
    User._meta.original_attrs['db_table'] = 'users'
    User.groups.db_table = 'user_groups'
    User.user_permissions.db_table = 'user_permissions'

    Group._meta.db_table = 'groups'
    Group._meta.original_attrs['db_table'] = 'groups'
    Group.permissions.db_table = 'group_permissions'

    Permission._meta.db_table = 'permissions'
    Permission._meta.original_attrs['db_table'] = 'permissions'

    LogEntry._meta.db_table = 'admin_log'
    LogEntry._meta.original_attrs['db_table'] = 'admin_log'

    Session._meta.db_table = 'sessions'
    Session._meta.original_attrs['db_table'] = 'sessions'

    ContentType._meta.db_table = 'content_types'
    ContentType._meta.original_attrs['db_table'] = 'content_types'

    MigrationRecorder._migration_class._meta.db_table = 'migrations'
    MigrationRecorder._migration_class._meta.original_attrs['db_table'] = 'migrations'
