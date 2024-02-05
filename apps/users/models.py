from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from utils.image_path import upload_avatar_for_user


class CustomUser(AbstractUser):
    display_name = models.CharField(
        max_length=50,
        verbose_name="отображаемое имя",
    )
    avatar = models.ImageField(
        upload_to=upload_avatar_for_user,
        verbose_name="Аватарка",
    )

    def delete(self, using=None, keep_parents=False):
        os.remove(self.avatar.path)
        super().delete(using=None, keep_parents=False)

    def __str__(self):
        return self.username

