# Generated by Django 4.0.1 on 2022-01-18 12:34

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naglowek',
            name='text_alt',
        ),
        migrations.AddField(
            model_name='naglowek',
            name='logo',
            field=models.ImageField(null=True, upload_to='logo'),
        ),
        migrations.AlterField(
            model_name='naglowek',
            name='dzielnica',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
