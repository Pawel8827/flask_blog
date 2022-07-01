# Generated by Django 4.0.1 on 2022-01-18 14:49

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_remove_naglowek_text_alt_naglowek_logo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='naglowek',
            name='dzielnica',
            field=models.TextField(default='test'),
        ),
        migrations.AlterField(
            model_name='naglowek',
            name='logo',
            field=models.ImageField(null=True, storage=django.core.files.storage.FileSystemStorage(location='info/static/img/logo'), upload_to='logo'),
        ),
    ]
