# Generated by Django 4.2.2 on 2023-07-06 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_users_alter_carstore_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='eid',
            new_name='epassword',
        ),
    ]
