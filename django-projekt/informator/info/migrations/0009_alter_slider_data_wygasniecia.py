# Generated by Django 4.0.1 on 2022-01-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_alter_slider_czas_wyswietalnia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='Data_wygasniecia',
            field=models.DateField(blank=True, null=True),
        ),
    ]
