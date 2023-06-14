# Generated by Django 3.2.16 on 2023-06-14 09:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('birthday', '0004_alter_birthdaymodel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthdaymodel',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор записи'),
        ),
    ]
