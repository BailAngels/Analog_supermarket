# Generated by Django 5.0.1 on 2024-02-13 06:58

import utils.image_path
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(upload_to=utils.image_path.upload_avatar_for_user, verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='display_name',
            field=models.CharField(max_length=50, verbose_name='Отображение имя'),
        ),
    ]