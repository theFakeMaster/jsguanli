import xadmin
from .models import *
from django.contrib.admin.models import LogEntry
from xadmin.views import BaseAdminView, CommAdminView
from xadmin.plugins.actions import BaseActionView
# Register your models here.

class UserinfoAdmin(object):
    list_display = ('name','userid','email','sex','c_time','idtype')# 字段在列表的显示
    search_fields = ['name','idtype','userid'] #同过name、idtype、userid进行查找
    list_filter =('idtype', 'sex','c_time') #过滤器
    list_per_page = 10  # 默认为10条

class UploadfileAdmin(object):
    list_display = ('username','headImg')
    list_per_page = 10  

class CourseAdmin(object):
    list_display = ('id','coursename')
    list_per_page = 10

class NoticesAdmin(object):
    list_display = ('id','p_name','r_time','p_content')
    search_fields = ['p_name'] 
    list_filter =('p_name', 'r_time') #过滤器
    list_per_page = 10

class NewsAdmin(object):
    list_display = ('id','news_title','news_author','r_time','news_picture','news_content')
    search_fields = ['news_title','news_author',] 
    list_filter =('news_title', 'news_author','r_time') #过滤器
    list_per_page = 10

class MessagesAdmin(object):
    list_display = ('id','s_name','t_name','date','time','content','direction')
    search_fields = ['s_name','t_name'] 
    list_filter =('s_name', 't_name','date','time') #过滤器
    list_per_page = 10

class LogEntryAdmin(object):
    list_display = ['object_repr','object_id','action_flag','user','change_message']

class ThemeSetting(object):
    enable_themes = True
    use_bootswatch = True

class CustomView(object):
    site_title = '教师教务管理系统后台'   # 网页头部导航
    site_footer = '教师教务管理系统'      # 底部版权内容
    # menu_style = 'accordion'  # 左侧导航折叠框

#绑定到xadmin的views.BaseAdminView
xadmin.site.register(BaseAdminView, ThemeSetting)
xadmin.site.register(CommAdminView, CustomView)

xadmin.site.site_header = '教师教务管理系统后台'
xadmin.site.register(Userinfo,UserinfoAdmin)
xadmin.site.register(Uploadfile,UploadfileAdmin)
xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Notices,NoticesAdmin)
xadmin.site.register(News,NewsAdmin)
xadmin.site.register(Messages,MessagesAdmin)
xadmin.site.register(LogEntry,LogEntryAdmin)


