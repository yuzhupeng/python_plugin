"""DjangoExam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf.urls import url
from exam import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index),#默认访问首页
    url('index/',views.index,name='index'),
    url('studentLogin/',views.studentLogin,name='studentLogin'),#学生登录
    url('startExam/',views.startExam,name='startExam'),#开始考试
    url('calculateGrade/',views.calculateGrade,name='calculateGrade'),#考试评分
    path('stulogout/',views.stulogout,name='stulogout'), # 学生退出登录
    path('userfile/',views.userfile,name='userfile'), # 个人信息
    path('examinfo/',views.examinfo,name='examinfo'), # 考试信息
]
