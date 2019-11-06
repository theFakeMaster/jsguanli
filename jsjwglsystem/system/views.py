from django.shortcuts import render,redirect,reverse,HttpResponseRedirect,HttpResponse
from .models import *
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.contrib.auth import authenticate, login as login1, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
import os,os.path
import time
# Create your views here.

# 注册
def register(request):
    if request.method == 'GET':
        form = Zhuce(request.POST,request.FILES)
        form.fields['username'].help_text = None
        return render(request, 'system/register.html', {'form': form})
    else:
        form = Zhuce(request.POST,request.FILES)
        if form.is_valid():
            sex = request.POST.get('sex')
            idtype = request.POST.get('idtype')
            userid = request.POST.get('userid')
            email = request.POST.get('email')
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            data = form.cleaned_data
            User.objects.create_user(username=data['username'], password=data['password'],email=data['email'])
            Userinfo.objects.create(name=data['username'], password=make_password(data['password']),email=data['email'],sex=sex,idtype=idtype,userid=userid)
            return redirect(reverse('system:login'))
        else:
            error = form.errors
            return render(request, 'system/register.html',{'form':form,'errors':error})

# 登陆
@csrf_exempt
def login(request):
    if request.method == "GET":
        form = Login()
        return render(request, 'system/login.html', {'form': form})
    else:
        form = Login(request.POST)
        if form.is_valid():
            # 成功
            login1(request, form.user)
            return redirect(reverse('system:index'))
        else:
            # 验证失败
            return render(request, 'system/login.html', {'form': form})

# 退出登录
def loginout(request):
    logout(request)
    return redirect(reverse('system:index'))

#主页
def index(request):
    if request.method == 'GET':
        username = request.user.username
        is_staff = request.user.is_staff
        userinfo = Userinfo.objects.filter(name=username)
        newcount = News.objects.all().count()
        somenew = News.objects.all().last()
        noticecount = Notices.objects.all().count()
        somenotice = Notices.objects.all().last()
        if is_staff == True:
            return render(request,'system/index.html',{'username': username, 'is_staff': is_staff,'userinfo':userinfo})
        else:
            userdict = Userinfo.objects.filter(name=username).values('idtype')[0]
            for useridtype in userdict.values():
                pass
            if useridtype == '0':
                messageself = Messages.objects.filter(t_name=username).count()
                somemessage = Messages.objects.filter(t_name=username).last()
                return render(request,'system/index.html',{'username': username, 'is_staff': is_staff,'userinfo':userinfo,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype})
            else:
                messageself = Messages.objects.filter(s_name=username).count()
                somemessage = Messages.objects.filter(s_name=username).last()
                return render(request,'system/index.html',{'username': username, 'is_staff': is_staff,'userinfo':userinfo,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype})
        
#上传文件
def upload(request):
    u_name = request.user.username
    if u_name == '':
        messages.error(request, '请您先注册登录,才能使用该功能。')
        return redirect('/')
    else:
        if request.method == "POST":
            u_name = request.user.username
            is_staff = request.user.is_staff
            uf = UploadfileForm(request.POST,request.FILES) #还没有查到是什么意思
            #判断是否为有效的
            if uf.is_valid():
                #获取表单元素
                username = uf.cleaned_data['username']
                headImg = uf.cleaned_data['headImg']
                if username == u_name:
                    # 写入数据库
                    Uploadfile.objects.create(username=username, headImg=headImg)
                    messages.error(request, '该文件上传成功!')
                    return redirect('/upload/')
                else:
                    messages.error(request, '您不能使用其他人的用户名进行上传!')
                    return redirect('/upload/')
        else:
            u_name = request.user.username
            is_staff = request.user.is_staff
            uf = UploadfileForm()
            newcount = News.objects.all().count()
            somenew = News.objects.all().last()
            noticecount = Notices.objects.all().count()
            somenotice = Notices.objects.all().last()
            userdict = Userinfo.objects.filter(name=u_name).values('idtype')[0]
            for useridtype in userdict.values():
                pass
            if useridtype == '0':
                messageself = Messages.objects.filter(t_name=u_name).count()
                somemessage = Messages.objects.filter(t_name=u_name).last()
                return render(request,'system/upload.html',{'username': u_name, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'uf':uf})
            else:
                messageself = Messages.objects.filter(s_name=u_name).count()
                somemessage = Messages.objects.filter(s_name=u_name).last()
                return render(request,'system/upload.html',{'username': u_name, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'uf':uf})

#文件库
def Filelibrary(request):
    username = request.user.username
    if username == '':
        messages.error(request, '请您先注册登录,才能使用该功能。')
        return redirect('/')
    else:
        is_staff = request.user.is_staff
        allfile = Uploadfile.objects.filter(username=username)
        newcount = News.objects.all().count()
        somenew = News.objects.all().last()
        noticecount = Notices.objects.all().count()
        somenotice = Notices.objects.all().last()
        userdict = Userinfo.objects.filter(name=username).values('idtype')[0]
        for useridtype in userdict.values():
            pass
        if useridtype == '0':
            messageself = Messages.objects.filter(t_name=username).count()
            somemessage = Messages.objects.filter(t_name=username).last()
            return render(request,'system/Filelibrary.html',{'username': username, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'allfile':allfile})
        else:
            messageself = Messages.objects.filter(s_name=username).count()
            somemessage = Messages.objects.filter(s_name=username).last()
            return render(request,'system/Filelibrary.html',{'username': username, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'allfile':allfile})

#文件删除
@csrf_exempt
def Delfile(request):
    username = request.user.username
    if username == '':
        messages.error(request, '请您先注册登录,才能使用该功能。')
        return redirect('/')
    else:
        fileid = request.POST.get('fileid')
        filepath = request.POST.get('filepath')
        os.remove(filepath)#删除相对路径为filepath的文件
        Uploadfile.objects.filter(id=fileid).delete()#数据库删除id为fileid的文件
        messages.error(request, '该文件删除成功!')
        return redirect('/Filelibrary/')

#我的课程表
@csrf_exempt
def Mycurriculum(request):
    username = request.user.username
    if username == '':
        messages.error(request, '请您先注册登录,才能使用该功能。')
        return redirect('/')
    else:
        is_staff = request.user.is_staff
        courseone = Courseone.objects.all()
        coursetwo = Coursetwo.objects.all()
        coursethree = Coursethree.objects.all()
        coursefour = Coursefour.objects.all()
        newcount = News.objects.all().count()
        somenew = News.objects.all().last()
        noticecount = Notices.objects.all().count()
        somenotice = Notices.objects.all().last()
        userdict = Userinfo.objects.filter(name=username).values('idtype')[0]
        for useridtype in userdict.values():
            pass
        if useridtype == '0':
            messageself = Messages.objects.filter(t_name=username).count()
            somemessage = Messages.objects.filter(t_name=username).last()
            return render(request,'system/Mycurriculum.html',{'username': username, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'courseone':courseone,'coursetwo':coursetwo,'coursethree':coursethree,'coursefour':coursefour})
        else:
            messageself = Messages.objects.filter(s_name=username).count()
            somemessage = Messages.objects.filter(s_name=username).last()
            return render(request,'system/Mycurriculum.html',{'username': username, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'courseone':courseone,'coursetwo':coursetwo,'coursethree':coursethree,'coursefour':coursefour})

#重新编辑课程表
@csrf_exempt
def reedtioncurriculum(request):
    username = request.user.username
    if username == '':
        messages.error(request, '请您先注册登录,才能使用该功能。')
        return redirect('/')
    else:
        if request.method == 'GET':
            is_staff = request.user.is_staff
            courselist = Course.objects.all()
            newcount = News.objects.all().count()
            somenew = News.objects.all().last()
            noticecount = Notices.objects.all().count()
            somenotice = Notices.objects.all().last()
            userdict = Userinfo.objects.filter(name=username).values('idtype')[0]
            for useridtype in userdict.values():
                pass
            if useridtype == '0':
                messageself = Messages.objects.filter(t_name=username).count()
                somemessage = Messages.objects.filter(t_name=username).last()
                return render(request,'system/reedtioncurriculum.html',{'username': username, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'courselist':courselist})
            else:
                messageself = Messages.objects.filter(s_name=username).count()
                somemessage = Messages.objects.filter(s_name=username).last()
                return render(request,'system/reedtioncurriculum.html',{'username': username, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'courselist':courselist})
        else:
            username = request.user.username
            is_staff = request.user.is_staff
            courselist = Course.objects.all()

            monday_1 = request.POST.get('monday_1')
            tuesday_1 = request.POST.get('tuesday_1')
            wednesday_1 = request.POST.get('wednesday_1')
            thursday_1 = request.POST.get('thursday_1')
            friday_1 = request.POST.get('friday_1')
            saturday_1 = request.POST.get('saturday_1')
            sunday_1 = request.POST.get('sunday_1')

            # bulk_create缺少主键,用for迭代数据表中的两个数据（id,coursename）,zip函数可以将多个可迭代对象封装成多元素的元组的列表，从而方便并行操作数据,这里将a、range（1,9）
            courseonelist = []
            a = [monday_1,tuesday_1,wednesday_1,thursday_1,friday_1,saturday_1,sunday_1]
            for n,m in zip(a,range(1,9)):
                obj1 = Courseone(
                    id = m,
                    coursename = n,
                )   
                courseonelist.append(obj1)

            monday_2 = request.POST.get('monday_2')
            tuesday_2 = request.POST.get('tuesday_2')
            wednesday_2 = request.POST.get('wednesday_2')
            thursday_2 = request.POST.get('thursday_2')
            friday_2 = request.POST.get('friday_2')
            saturday_2 = request.POST.get('saturday_2')
            sunday_2 = request.POST.get('sunday_2')

            coursetwolist = []
            a = [monday_2,tuesday_2,wednesday_2,thursday_2,friday_2,saturday_2,sunday_2]
            for n,m in zip(a,range(1,9)):
                obj2 = Coursetwo(
                    id = m,
                    coursename = n,
                )   
                coursetwolist.append(obj2)

            monday_3 = request.POST.get('monday_3')
            tuesday_3 = request.POST.get('tuesday_3')
            wednesday_3 = request.POST.get('wednesday_3')
            thursday_3 = request.POST.get('thursday_3')
            friday_3 = request.POST.get('friday_3')
            saturday_3 = request.POST.get('saturday_3')
            sunday_3 = request.POST.get('sunday_3')
            
            coursethreelist = []
            a = [monday_3,tuesday_3,wednesday_3,thursday_3,friday_3,saturday_3,sunday_3]
            for n,m in zip(a,range(1,9)):
                obj3 = Coursethree(
                    id = m,
                    coursename = n,
                )   
                coursethreelist.append(obj3)

            monday_4 = request.POST.get('monday_4')
            tuesday_4 = request.POST.get('tuesday_4')
            wednesday_4 = request.POST.get('wednesday_4')
            thursday_4 = request.POST.get('thursday_4')
            friday_4 = request.POST.get('friday_4')
            saturday_4 = request.POST.get('saturday_4')
            sunday_4 = request.POST.get('sunday_4')
            coursefourlist = [monday_4,tuesday_4,wednesday_4,thursday_4,friday_4,saturday_4,sunday_4]

            coursefourlist = []
            a = [monday_4,tuesday_4,wednesday_4,thursday_4,friday_4,saturday_4,sunday_4]
            for n,m in zip(a,range(1,9)):
                obj4 = Coursefour(
                    id = m,
                    coursename = n,
                )   
                coursefourlist.append(obj4)

            try:                                            #可能存在数据重复的问题
                Courseone.objects.bulk_create(courseonelist)#用bulk_create将多条数据同时写入数据库
            except:                                             
                Courseone.objects.all().delete()            #先删再创建,无法使用update()批量更新    
                Courseone.objects.bulk_create(courseonelist)

            try:
                Coursetwo.objects.bulk_create(coursetwolist)
            except:
                Coursetwo.objects.all().delete()
                Coursetwo.objects.bulk_create(coursetwolist)

            try:
                Coursethree.objects.bulk_create(coursethreelist)
            except:
                Coursethree.objects.all().delete()
                Coursethree.objects.bulk_create(coursethreelist)

            try:
                Coursefour.objects.bulk_create(coursefourlist)
            except:
                Coursefour.objects.all().delete()
                Coursefour.objects.bulk_create(coursefourlist)
        
            messages.error(request, '提交成功！')
            return redirect('/Mycurriculum/')

#通知页面
@csrf_exempt
def notice(request):
    username = request.user.username
    if username == '':
        messages.error(request, '请您先注册登录,才能使用该功能。')
        return redirect('/')
    else:
        if request.method == 'GET':
            is_staff = request.user.is_staff
            notices_all = Notices.objects.all().order_by('-r_time')
            newcount = News.objects.all().count()
            somenew = News.objects.all().last()
            noticecount = Notices.objects.all().count()
            somenotice = Notices.objects.all().last()
            userdict = Userinfo.objects.filter(name=username).values('idtype')[0]
            for useridtype in userdict.values():
                pass
            if useridtype == '0':
                messageself = Messages.objects.filter(t_name=username).count()
                somemessage = Messages.objects.filter(t_name=username).last()
                return render(request,'system/Notice.html',{'username': username, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'notices_all':notices_all})
            else:
                messageself = Messages.objects.filter(s_name=username).count()
                somemessage = Messages.objects.filter(s_name=username).last()
                return render(request,'system/Notice.html',{'username': username, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'notices_all':notices_all})
        else:
            username = request.user.username
            p_name = username
            r_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            p_content = request.POST.get('p_content')
            
            Notices.objects.update_or_create(p_name=p_name,r_time=r_time,p_content=p_content)

            messages.error(request, '提交成功！')
            return redirect('/notice/')

#删除通知
@csrf_exempt
def delnotice(request):
    username = request.user.username
    if username == '':
        messages.error(request, '请您先注册登录,才能使用该功能。')
        return redirect('/')
    else:
        noticeid = request.POST.get('noticeid')
        Notices.objects.filter(id=noticeid).delete()
        messages.error(request, '此条通知删除成功!')
        return redirect('/notice/')

#新闻
@csrf_exempt
def news(request):
    if request.method == 'GET':
        username = request.user.username
        is_staff = request.user.is_staff
        new_uf = NewuploadfileForm(request.POST,request.FILES) #还没有查到是什么意思
        newsall = News.objects.all()
        newcount = News.objects.all().count()
        somenew = News.objects.all().last()
        noticecount = Notices.objects.all().count()
        somenotice = Notices.objects.all().last()
        userdict = Userinfo.objects.filter(name=username).values('idtype')[0]
        for useridtype in userdict.values():
            pass
        if useridtype == '0':
            messageself = Messages.objects.filter(t_name=username).count()
            somemessage = Messages.objects.filter(t_name=username).last()
            return render(request,'system/News.html',{'username': username, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'new_uf':new_uf,'newsall':newsall})
        else:
            messageself = Messages.objects.filter(s_name=username).count()
            somemessage = Messages.objects.filter(s_name=username).last()
            return render(request,'system/News.html',{'username': username, 'is_staff': is_staff,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype,'new_uf':new_uf,'newsall':newsall})
    else:
        username = request.user.username
        is_staff = request.user.is_staff
        new_uf = NewuploadfileForm(request.POST,request.FILES) #还没有查到是什么意思
        #判断是否为有效的
        if new_uf.is_valid():
            #获取表单元素
            news_title = new_uf.cleaned_data['news_title']
            username = request.user.username
            news_author = username
            r_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            news_picture = new_uf.cleaned_data['news_picture']
            news_content = new_uf.cleaned_data['news_content']
            # 写入数据库
            News.objects.create(news_title=news_title, news_author=news_author,r_time=r_time,news_picture=news_picture,news_content=news_content)
            messages.error(request, '新闻发布成功')
            return redirect('/news/')
        else:
            messages.error(request, '新闻发布失败')
            return redirect('/news/')

#删除新闻
@csrf_exempt
def delnews(request):
    username = request.user.username
    if username == '':
        messages.error(request, '请您先注册登录,才能使用该功能。')
        return redirect('/')
    else:
        newsid = request.POST.get('newsid')
        newimgurl = request.POST.get('newimgurl')
        os.remove(newimgurl)
        News.objects.filter(id=newsid).delete()
        messages.error(request, '此条新闻删除成功!')
        return redirect('/news/',{'messages':messages})

#编辑留言
@csrf_exempt
def edmessage(request):
    username = request.user.username
    if username == '':
        messages.error(request, '请您先注册登录,才能使用该功能。')
        return redirect('/')
    else:
        if request.method == 'GET':
            is_staff = request.user.is_staff
            student_all = Userinfo.objects.filter(idtype=1)
            teacher_all = Userinfo.objects.filter(idtype=0)
            newcount = News.objects.all().count()
            somenew = News.objects.all().last()
            noticecount = Notices.objects.all().count()
            somenotice = Notices.objects.all().last()
            datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            date = datetime.split(' ')[0]
            userdict = Userinfo.objects.filter(name=username).values('idtype')[0]
            for useridtype in userdict.values():
                pass
            if useridtype == '0':
                messageself = Messages.objects.filter(t_name=username).count()
                somemessage = Messages.objects.filter(t_name=username).last()
                return render(request,'system/edmessage.html',{'username':username,'is_staff':is_staff,'student_all':student_all,'teacher_all':teacher_all,'useridtype':useridtype,'date':date,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype})
            else:
                messageself = Messages.objects.filter(s_name=username).count()
                somemessage = Messages.objects.filter(s_name=username).last()
                return render(request,'system/edmessage.html',{'username':username,'is_staff':is_staff,'student_all':student_all,'teacher_all':teacher_all,'useridtype':useridtype,'date':date,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype})
        else:
            username = request.user.username
            userdict = Userinfo.objects.filter(name=username).values('idtype')[0]
            for useridtype in userdict.values():
                pass
            if useridtype == '0':
                s_name = request.POST.get('messageed')
                t_name = request.user.username
                datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                date = datetime.split(' ')[0]
                s_time = datetime.split(' ')[1]
                content = request.POST.get('content')
                direction = '1'
                Messages.objects.create(s_name=s_name,t_name=t_name,date=date,time=s_time,content=content,direction=direction)
            else:
                t_name = request.POST.get('messageed')
                s_name = request.user.username
                datetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                date = datetime.split(' ')[0]
                s_time = datetime.split(' ')[1]
                content = request.POST.get('content')
                direction = '0'
                Messages.objects.create(s_name=s_name,t_name=t_name,date=date,time=s_time,content=content,direction=direction)
            return redirect('/edmessage/')

#查看留言
@csrf_exempt
def message(request):
    username = request.user.username
    if username == '':
        messages.error(request, '请您先注册登录,才能使用该功能。')
        return redirect('/')
    else:
        is_staff = request.user.is_staff
        messageed = request.GET.get('messageed')   
        userdict = Userinfo.objects.filter(name=username).values('idtype')[0]
        student_all = Userinfo.objects.filter(idtype=1)
        teacher_all = Userinfo.objects.filter(idtype=0)
        newcount = News.objects.all().count()
        somenew = News.objects.all().last()
        noticecount = Notices.objects.all().count()
        somenotice = Notices.objects.all().last()
        for useridtype in userdict.values():
            pass
        if useridtype == '0':
            messages_2 = Messages.objects.filter(t_name=username,s_name=messageed)
            messageself = Messages.objects.filter(t_name=username).count()
            somemessage = Messages.objects.filter(t_name=username).last()
            return render(request,'system/message.html',{'username':username,'is_staff':is_staff,'student_all':student_all,'teacher_all':teacher_all,'useridtype':useridtype,'messages_2':messages_2,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype})
        else:
            messages_2 = Messages.objects.filter(t_name=messageed,s_name=username)
            messageself = Messages.objects.filter(s_name=username).count()
            somemessage = Messages.objects.filter(s_name=username).last()
            return render(request,'system/message.html',{'username':username,'is_staff':is_staff,'student_all':student_all,'teacher_all':teacher_all,'useridtype':useridtype,'messages_2':messages_2,'newcount':newcount,'noticecount':noticecount,'messageself':messageself,'somenew':somenew,'somenotice':somenotice,'somemessage':somemessage,'useridtype':useridtype})

        
        
        