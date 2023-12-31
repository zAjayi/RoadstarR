# Generated by Django 4.2.2 on 2023-07-07 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_users_userinfo_alter_userinfo_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=100)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=15)),
                ('emessage', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'contactinfo',
            },
        ),
    ]
