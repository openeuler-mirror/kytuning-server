"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token



urlpatterns = [
    # path('admin/', admin.site.urls),
    path('kytuning/', include('appStore.api.router')),

    # url(r'^kytuning/login/', include('rest_framework.urls', namespace='rest_framework')),
    # 登陆退出接口^api-auth/ ^login/$ [name='login']  #^api-auth/ ^logout/$ [name='logout']
    url(r'^kytuning/api-token-auth/', obtain_jwt_token),  # 生成token
    url(r'^kytuning/api-token-refresh/', refresh_jwt_token),  # 刷新token
    url(r'^kytuning/api-token-verify/', verify_jwt_token),  # 验证token
]
