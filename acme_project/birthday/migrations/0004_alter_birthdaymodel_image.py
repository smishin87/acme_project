# Generated by Django 3.2.16 on 2023-06-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0003_auto_20230609_1846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthdaymodel',
            name='image',
            field=models.ImageField(blank=True, upload_to='birthday_images', verbose_name='фото'),
        ),
    ]
