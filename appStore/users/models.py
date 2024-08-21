from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
# 能否只取一层,不行就写字段
# class UserProfileGroup(models.Model):
#     """用户组"""
#     name = models.CharField(unique=True, max_length=32)
#
#     class Meta:
#         db_table = 'user_profile_group'


class UserProfile(AbstractUser):
    """
    用户模型类
    """
    user_phone = models.CharField(unique=True,null=True, max_length=22, verbose_name='手机号')
    chinese_name = models.CharField(max_length=255, unique=True)
    is_superuser = models.BooleanField(default=False, verbose_name='是否是管理员')

    class Meta:
        db_table = 'user_profile'