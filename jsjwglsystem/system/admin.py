# from django.contrib import admin
# from .models import *
# from django.contrib.admin.models import LogEntry
# from xadmin.views import BaseAdminView, CommAdminView
# from xadmin.plugins.actions import BaseActionView
# # Register your models here.

# class UserinfoAdmin(admin.ModelAdmin):
#     list_display = ('name','userid','email','sex','c_time','idtype')# 字段在列表的显示
#     search_fields = ['name','idtype','userid'] #同过name、idtype、userid进行查找
#     list_filter =('idtype', 'sex','c_time') #过滤器
#     list_per_page = 10  # 默认为10条

# class UploadfileAdmin(admin.ModelAdmin):
#     list_display = ('username','headImg')
#     list_filter =('username') 
#     list_per_page = 10  

# class CourseAdmin(admin.ModelAdmin):
#     list_display = ('coursename')
#     list_per_page = 10

# class ClassinfoAdmin(admin.ModelAdmin):
#     list_display = ('classname')
#     list_per_page = 10

# class ClasslocationsAdmin(admin.ModelAdmin):
#     list_display = ('classlocations')
#     list_per_page = 10

# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('teachername')
#     list_per_page = 10

# # xadmin 无法进行外键搜索请问是什么原因 Unable to lookup#
# #需要改写 '外键字段名__关联表的具体字段名’，注意是双下划线 __#

# # class TeacherscheduleAdmin(object):
# #     list_display = ('coursename','classname','classlocations','week')
# #     search_fields = ['coursename__coursename','classname__classname','classlocations__classlocations','week'] 
# #     list_filter =('coursename__coursename','classname__classname','classlocations__classlocations','week') 
# #     list_per_page = 10

# # class StudentscheduleAdmin(object):
# #     list_display = ('teachername','coursename','classlocations','week')
# #     search_fields = ['teachername__teachername','coursename__coursename','classlocations__classlocations','week'] 
# #     list_filter =('teachername__teachername','teachername__coursename','classlocations__classlocations','week') 
# #     list_per_page = 10

# class LogEntryAdmin(admin.ModelAdmin):
#     list_display = ['object_repr','object_id','action_flag','user','change_message']

# class ThemeSetting(object):
#     enable_themes = True
#     use_bootswatch = True

# class CustomView(admin.ModelAdmin):
#     site_title = '教师教务管理系统后台'   # 网页头部导航
#     site_footer = '教师教务管理系统'      # 底部版权内容
#     # menu_style = 'accordion'  # 左侧导航折叠框

# #绑定到xadmin的views.BaseAdminView
# admin.site.register(BaseAdminView, ThemeSetting)
# admin.site.register(CommAdminView, CustomView)

# admin.site.site_header = '教师教务管理系统后台'
# admin.site.register(Userinfo,UserinfoAdmin)
# admin.site.register(Uploadfile,UploadfileAdmin)
# admin.site.register(Course,CourseAdmin)
# admin.site.register(Classinfo,ClassinfoAdmin)
# admin.site.register(Classlocations,ClasslocationsAdmin)
# admin.site.register(Teacher,TeacherAdmin)
# # xadmin.site.register(Teacherschedule,TeacherscheduleAdmin)
# # xadmin.site.register(Studentschedule,StudentscheduleAdmin)
# admin.site.register(LogEntry,LogEntryAdmin)


