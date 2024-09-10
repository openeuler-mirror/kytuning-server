from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    """
    用户模型类
    """
    user_phone = models.CharField(unique=True, null=True, max_length=22, verbose_name='手机号')
    chinese_name = models.CharField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False, verbose_name='是否是管理员')

    class Meta:
        db_table = 'user_profile'