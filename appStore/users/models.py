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
    user_type_choices = (
        (1, '普通用户'),
        (2, '管理员'),
    )
    # user_group_id = models.IntegerField(null=True,verbose_name='用户组id')
    user_phone = models.CharField(unique=True,null=True, max_length=22, verbose_name='手机号')
    is_superuser = models.BooleanField(default=True, verbose_name='是否是管理员')
    is_staff = models.BooleanField(default=True, verbose_name='是否是员工')
    # user_type = models.IntegerField(choices=user_type_choices, verbose_name='用户类型')

    class Meta:
        db_table = 'user_profile'