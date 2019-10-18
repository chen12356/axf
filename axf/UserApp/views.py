import re
import uuid


from PIL import ImageFont,  Image
from PIL.ImageDraw import ImageDraw
from django.contrib.auth.hashers import make_password, check_password

from django.core.cache import cache
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.template import loader
from django.urls import reverse
from django.utils.six import BytesIO

from UserApp.models import Axf_user
from UserApp.view_constaint import send_email
from axf import settings


def register(request):
    if request.method == 'GET':
        return render(request,'axf/user/register/register.html')
    if request.method == 'POST':

        name = request.POST.get('name')
        password = request.POST.get('password')
        # 对密码进行加密,保存到数据库
        password = make_password(password)
        email = request.POST.get('email')
        icon = request.FILES.get('icon')
        # 生成一个唯一字符串,用于邮件激活的传输参数,避免敏感信息透露
        token = uuid.uuid4()
        user = Axf_user()
        user.u_name = name
        user.u_password = password
        user.u_email = email
        user.u_icon = icon
        user.u_token = token
        user.save()
        # 注册成功,设置缓存,用于设定邮件过期时间
        cache.set(token,user.id,timeout=60)
        send_email(name,email,token)

        # 跳转到登录页面
        return render(request,'axf/user/login/login.html')



def checkName(request):
    name = request.GET.get('name')
    names = Axf_user.objects.filter(u_name=name)
    data = {
        'msg': '用户名可用',
        'status': 200,
    }
    if names.count() > 0:
    #     说明用户名存在,
        data['msg'] = '用户名已存在'
        data['status'] = 201

    return JsonResponse(data=data)



def login(request):
    if request.method == 'GET':
        return render(request,'axf/user/login/login.html')
    if request.method == 'POST':
        imgcode = request.POST.get('imgCode')
        #在生成验证码时,会保存在session中
        verify_code = request.session.get('verify_code')
        #为了友好性,验证码比较不区分大小写,需要注意match和search在判断是区别
        b = re.match(imgcode,verify_code,re.I)
        context = {
            'msg':'ok',
        }
        if b:
            # 建议使用用户名和密码分开比较,可以减少访问数据库.
            name = request.POST.get('name')
            users = Axf_user.objects.filter(u_name=name)
            if users.count() > 0:
                password = request.POST.get('password')
                user = users.first()
                if check_password(password,user.u_password):
                #     密码验证成功,那么需要判断激活状态
                    if user.u_active == True:
                        # print(user.u_icon)
                        # context['name'] = user.u_name
                        # context['new_icon'] = '/static/upload/'+str(user.u_icon)
                        # context['status'] = 200
                        # return redirect(request,'axf/main/mine/mine.html',context)

                        #上面方法直接给页面返回数据，不建议使用，因为其他页面可能也会需要登录
                        # 使用session来做
                        request.session['user_id'] = user.id
                        return redirect(reverse('axfmine:mine'))
                    else:
                        context['msg'] = '该用户未激活,请立刻前往邮箱激活账户 ^_^'
                        return render(request, 'axf/user/login/login.html', context=context)
                else:
                    context['msg'] = '密码输入错误'
                    return render(request, 'axf/user/login/login.html', context=context)
            else:
                context['msg'] = '该用户名不存在'
                return render(request, 'axf/user/login/login.html', context=context)
        else:
            context['msg'] = '验证码输入错误'
            return render(request,'axf/user/login/login.html',context=context)

def testmail(request):
    subject = '激活'
    message = '测试成功'
    context = {
        'name':'强',
        'url':'http://127.0.0.1:8000/axfuser/checkEmail/'
    }
    html_message = loader.get_template('active.html').render(context=context)
    from_email = 'ccq1406159466@163.com'
    recipient_list = ['ccq1406159466@163.com']

    send_mail(subject=subject,message=message,html_message=html_message,from_email=from_email,recipient_list=recipient_list)
    return HttpResponse('发送成功')


def checkEmail(request):
    token = request.GET.get('token')
    user_id = cache.get(token)
    if user_id:
        # return HttpResponse('邮件激活成功')
        user = Axf_user.objects.get(pk=user_id)
        user.u_active = True
        user.save()
        #删除缓存
        cache.delete(token)
        return HttpResponse('激活成功')
    return HttpResponse('邮件已过期')

# //获取验证码的方法

def get_code(request):

    # 初始化画布，初始化画笔

    mode = "RGB"

    size = (200, 100)

    red = get_color()

    green = get_color()

    blue = get_color()

    color_bg = (red, green, blue)

    image = Image.new(mode=mode, size=size, color=color_bg)

    imagedraw = ImageDraw(image, mode=mode)

    imagefont = ImageFont.truetype(settings.FONT_PATH, 100)

    verify_code = generate_code()

    request.session['verify_code'] = verify_code

    for i in range(4):
        fill = (get_color(), get_color(), get_color())
        imagedraw.text(xy=(50*i, 0), text=verify_code[i], font=imagefont, fill=fill)

    for i in range(100):
        fill = (get_color(), get_color(), get_color())
        xy = (random.randrange(201), random.randrange(100))
        imagedraw.point(xy=xy, fill=fill)

    fp = BytesIO()

    image.save(fp, "png")

    return HttpResponse(fp.getvalue(), content_type="image/png")




import random

def get_color():
    return random.randrange(256)

def generate_code():
    source = "qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM"

    code = ""

    for i in range(4):
        code += random.choice(source)

    return code


def payment(request):
    return render(request,'axf/user/payment/payment.html')