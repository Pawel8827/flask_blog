# Generated by Django 4.0.1 on 2022-01-27 12:53

import ckeditor.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_naglowek_unike_alter_slider_kolor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='Wielkosc',
        ),
        migrations.AddField(
            model_name='slider',
            name='Czas_wyswietalnia',
            field=models.ImageField(default='5', upload_to=''),
        ),
        migrations.AddField(
            model_name='slider',
            name='Data_Utworzenia',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='Data_wygasniecia',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='slider',
            name='Text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]