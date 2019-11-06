from django.urls import path
from django.conf.urls import url
from . import views

app_name = "system"

urlpatterns = [
    path('', views.index, name="index"),#主页
    path('login/',views.login, name="login"),#登陆
    path('loginout/', views.loginout , name='loginout'), #退出
    path('upload/',views.upload , name="upload"),#上传文件
    path('register/',views.register,name="register"),#注册
    path('Filelibrary/',views.Filelibrary,name='Filelibrary'),#文件库
    path('Delfile/',views.Delfile,name='Delfile'),#文件删除
    path('Mycurriculum/',views.Mycurriculum,name='Mycurriculum'),#查看课程表
    path('Mycurriculum/reedtioncurriculum/',views.reedtioncurriculum,name='reedtioncurriculum'),#重新编辑课程表
    path('reedtioncurriculum/',views.reedtioncurriculum,name='reedtioncurriculum'),#提交表单
    path('notice/',views.notice,name='notice'),#通知
    path('delnotice/',views.delnotice,name='delnotice'),#通知删除
    path('news/',views.news,name='name'),#新闻
    path('delnews/',views.delnews,name='delnews'),#新闻删除
    path('edmessage/',views.edmessage,name='edmessage'),#编辑消息
    path('message/',views.message,name='message'),#选择联系人
]