# Generated by Django 4.2.2 on 2023-07-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400)),
                ('price', models.CharField(max_length=400)),
                ('imageUrl', models.URLField(max_length=1000)),
            ],
        ),
    ]