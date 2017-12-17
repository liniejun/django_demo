# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import *
from hashlib import sha1

# Create your views here.
def register(request):
    return render(request, 'df_user/register.html', '')

def register_handle(request):
    # 接收用户输入
    post = request.POST
    uname = post.get('user_name')
    upwd = post.get('pwd')
    ucpwd = post.get('cpwd')
    uemail = post.get('email')
    uphone = post.get('phone')

    # 判断密码
    if upwd != ucpwd:
        return redirect('register')

    # 密码加密
    s1 = sha1()
    s1.update(upwd)
    usafepwd = s1.hexdigest()

    # 创建对象，保存到数据库
    user = UserInfo()
    user.df_name = uname
    user.df_pwd = usafepwd
    user.df_email = uemail
    user.df_phone = uphone
    user.save()

    #  注册成功跳转到登陆页面
    return redirect('/user/login')

def register_exist(request):
    uname = request.GET.get('user_name')
    count = UserInfo.objects.filter(df_name=uname).count
    return JsonResponse({'count': count})

def login(request):
    uname = request.COOKIES.get('user_name', '')
    context = {'title': '用户登录', 'error_name': 0, 'error_pwd': 0, 'df_name': uname, 'page_name': 1}
    return render(request, 'df_user/login.html', context)

def login_handle(request):
    # 接收用户请求信息
    post = request.POST
    uname = post.get('username')
    upwd = post.get('pwd')
    remember = post.get('remember', 0)

    # 根据用户名查询对象
    users = UserInfo.objects.filter(df_name=uname)
    print uname
    # 判断：如果未查找到用户名错，如果查到则判断密码是否正确，正确则跳转页面
    if len(users) == 1:
        s1 = sha1()
        s1.update(upwd)
        if s1.hexdigest() == users[0].df_pwd:
            red = HttpResponseRedirect('/user/info')
            # 记住用户名
            if remember != 0:
                red.set_cookie('user_name', uname)
            else:
                red.set_cookie('user_name','',max_age=-1)
            request.session['user_id'] = users[0].id
            request.session['user_name'] = uname
            return red
        else:
            context = {'title':'用户登录', 'error_name': 0, 'error_pwd': 1, 'df_name': uname, 'df_pwd': upwd, 'page_name': 1}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title': '用户登录', 'error_name': 1, 'error_pwd': 0, 'df_name': uname, 'df_pwd': upwd, 'page_name': 1}
        return render(request, 'df_user/login.html', context)



def info(request):
    user_email = UserInfo.objects.get(id=request.session['user_id']).df_email
    context = {'title':'用户中心', 'user_email': user_email, 'user_name': request.session['user_name'], 'page_name': 1}
    return render(request, 'df_user/user_center_info.html')

def order(request):
    context = {'title': '用户中心', 'page_name': 1}
    return render(request, 'df_user/user_center_order.html', context)

def site(request):
    user = UserInfo.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        post = request.POST
        user.df_sname = post.get('df_sname')
        user.df_addr = post.get('df_addr')
        user.df_emailCode = post.get('df_emailCode')
        user.save()
    context = {'title':'用户中心', 'user':user, 'page_name': 1}
    return render(request, 'df_user/user_center_site.html', context)