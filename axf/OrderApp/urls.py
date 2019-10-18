from django.conf.urls import url

from OrderApp import views

urlpatterns = [
    url(r'^order_detail/',views.order_detail),
    url(r'^make_order/',views.make_order),

#     测试支付
    url(r'^testpay/',views.testpay,name='testpay'),
#     跳转成功页面
    url(r'^pay_success/',views.pay_success),
]