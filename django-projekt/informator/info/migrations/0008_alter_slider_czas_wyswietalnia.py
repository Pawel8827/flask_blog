# Generated by Django 4.0.1 on 2022-01-27 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_remove_slider_wielkosc_slider_czas_wyswietalnia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='Czas_wyswietalnia',
            field=models.IntegerField(default=5),
        ),
    ]
