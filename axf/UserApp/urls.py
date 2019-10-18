from django.conf.urls import url

from UserApp import views

urlpatterns = [
    url(r'^register/',views.register,name='register'),
#     后端验证用户名
    url(r'^checkName/',views.checkName),
    #邮件过期时间
    url(r'^checkEmail/',views.checkEmail,name='checkEmail'),
    #测试发送邮件
    url(r'^testmail/',views.testmail),

    # 登录
    url(r'^login/', views.login, name='login'),
    # 图片验证码
    url(r'^get_code/',views.get_code,name='get_code'),

    # url(r'^checklogin/', views.checklogin),
#     订单页面
    url(r'^payment/',views.payment,name='payment')
]