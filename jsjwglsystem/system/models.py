from django.db import models
from django.contrib.auth.models import User
import django.utils.timezone as timezone

# Create your models here.

class Userinfo(models.Model):
    name = models.CharField(verbose_name='教师名',max_length=10)
    password = models.CharField(verbose_name='密码',max_length=16)
    userid = models.CharField(verbose_name='用户ID',max_length=16,default="")
    gender = (
        ('0', "男"),
        ('1', "女"),
    )
    email = models.EmailField(unique=True,default='')
    sex = models.CharField(verbose_name='性别',max_length=32, choices=gender, default="男")
    c_time = models.DateTimeField(verbose_name='创建日期',default=timezone.now)

    type = (
        ('0', "教师"),
        ('1', "学生"),
    )

    idtype = models.CharField(verbose_name='身份类别',max_length=32, choices=type, default="教师")
    userimg_fl = models.FileField(verbose_name='头像图片储存路径',upload_to = './usersimg/',default='')
    class Meta:
        verbose_name_plural="用户信息"

class Uploadfile(models.Model):
    username = models.CharField(verbose_name='用户名',max_length = 30)
    headImg = models.FileField(upload_to = './upload/')
    class Meta:
        verbose_name_plural = "上传文件"

class Course(models.Model):
    coursename = models.CharField(verbose_name='课程名',max_length = 20,null=True,blank=True)
    class Meta:
        verbose_name_plural="课程名表"

class Courseone(models.Model):
    id = models.IntegerField(primary_key = True)
    coursename = models.CharField(verbose_name="课程名",max_length = 20,null=True,blank=True)
    class Meta:
        verbose_name_plural = "顺序为1的课程表"

class Coursetwo(models.Model):
    id = models.IntegerField(primary_key = True)
    coursename = models.CharField(verbose_name="课程名",max_length = 20,null=True,blank=True)
    class Meta:
        verbose_name_plural = "顺序为2的课程表"

class Coursethree(models.Model):
    id = models.IntegerField(primary_key = True)
    coursename = models.CharField(verbose_name="课程名",max_length = 20,null=True,blank=True)
    class Meta:
        verbose_name_plural = "顺序为3的课程表"

class Coursefour(models.Model):
    id = models.IntegerField(primary_key = True)
    coursename = models.CharField(verbose_name="课程名",max_length = 20,null=True,blank=True)
    class Meta:
        verbose_name_plural = "顺序为4的课程表"

class Notices(models.Model):
    p_name = models.CharField(verbose_name='发布者名称',max_length = 10)
    r_time = models.DateTimeField(verbose_name='发布时间')
    p_content = models.TextField(verbose_name="发布内容",max_length=300)
    class Meta:
        verbose_name_plural = "通知"

class News(models.Model):
    news_title = models.CharField(verbose_name='新闻标题',max_length=20)
    news_author = models.CharField(verbose_name='新闻作者',max_length=10)
    r_time = models.DateTimeField(verbose_name='发布时间')
    news_picture = models.FileField(verbose_name='新闻图片储存路径',upload_to = './newsimg/')
    news_content = models.TextField(verbose_name='新闻内容',max_length=300)
    class Meta:
        verbose_name_plural = "新闻"

class Messages(models.Model):
    s_name = models.CharField(verbose_name='学生姓名',max_length=8)
    t_name = models.CharField(verbose_name='教师姓名',max_length=8)
    date = models.DateField(verbose_name='发布日期',auto_now_add=True)
    time = models.TimeField(verbose_name='发布时间',auto_now_add=True)
    content = models.TextField(verbose_name='发布内容',max_length=200)
    direction = models.CharField(verbose_name='消息的发送或接收',choices=(('0','学生给教师'),
    ('1','教师给学生')),max_length=20,default='0')
    class Meta:
        verbose_name_plural = '消息'
    




    

