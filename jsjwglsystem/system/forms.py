from .models import *
from django.forms import PasswordInput,CharField,Textarea,TextInput,ModelForm,Form,EmailInput
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django import forms
from captcha.fields import CaptchaField

class Zhuce(ModelForm):
    username = CharField(label='账户名',widget=TextInput(attrs={'placeholder':"用户名"}),error_messages={'required':u'账号重复'})
    password = CharField(widget=PasswordInput(attrs={'placeholder':"密码"}),label='密码')
    email = forms.EmailField(widget=EmailInput(attrs={'placeholder':"电子邮箱"}),label='电子邮箱')
    captcha = CaptchaField()
    
    class Meta:
        model = User
        fields = ['username','password','email']
        widgets = {
            'password': PasswordInput,
            'email':EmailInput,
        }
        labels = {
            'username': '用户名',
            'password': '密码',
            'email':'电子邮箱',
        }
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("name",None)
        username_list = User.objects.all().values_list('username')
        if username:
            for i in username_list:
                if username in i:
                    raise ValidationError(
                        '用户名已存在，请重新输入'
                    )
        return cleaned_data

class Login(Form):
    username = CharField(label='用户名',widget=TextInput(attrs={'placeholder':"用户名"}))
    password = CharField(widget=PasswordInput(attrs={'placeholder':"密码"}),label='密码')
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'password': PasswordInput
        }
    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username',None)
        password = cleaned_data.get('password',None)
        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise ValidationError('用户名密码错误')
            else:
                self.user=user

class UploadfileForm(forms.Form):
    username = forms.CharField(label='上传人姓名')
    headImg = forms.FileField(label='上传文件路径') 

class NewuploadfileForm(forms.Form):
    news_title = forms.CharField(label='新闻标题',max_length=20)
    news_picture = forms.FileField(label='新闻图片')
    news_content = forms.CharField(label='新闻内容',max_length=300)

    