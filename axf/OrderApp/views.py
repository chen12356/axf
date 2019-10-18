from alipay import AliPay
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from CartApp.models import Axf_cart
from CartApp.views import total_price
from OrderApp.models import Axf_order, Axf_order_goods
from axf.settings import APP_PRIVATE_KEY_STRING, APP_PUBLIC_KEY_STRING


def order_detail(request):
    order_id = request.GET.get('order_id')
    order = Axf_order.objects.get(pk=order_id)
    total_price = order.axf_order_goods_set.first().og_price
    context = {
        'order':order,
        'total_price':total_price
    }
    request.session['order_id'] = order_id
    request.session['total_price'] = total_price

    return render(request,'axf/order/order_detail.html',context=context)


def make_order(request):
    # 接收ajax的请求，
    data = {
        'msg':'ok',
        'status':200,
    }
    user_id = request.session.get('user_id')
    # 创建当前订单的对象
    order = Axf_order()
    order.o_user_id = user_id
    order.save()
    # 现在需要把购物车的选中的数据，存入订单商品表中
    carts = Axf_cart.objects.filter(c_user_id=user_id).filter(c_is_select=True)
    for cart in carts:
        orderGoods = Axf_order_goods()
        #如果按照订单商品表定义的属性来添加属性值，那么有外键的是对应的对象
        #或者按照表的来添加如：orderGoods.og_order_id = order.id
        orderGoods.og_order = order
        orderGoods.og_goods = cart.c_goods

        orderGoods.og_goods_num = cart.c_goods_num
        orderGoods.og_price = total_price(user_id)
        orderGoods.save()
        cart.delete()

    data['order_id'] = order.id
    return JsonResponse(data=data)

# 测试支付
def testpay(request):
    order_id = request.session.get('order_id')
    total_price = request.session.get('total_price')
    alipay = AliPay(
        appid="2016101200665417",
        app_notify_url=None,  # 默认回调url
        app_private_key_string=APP_PRIVATE_KEY_STRING,
        # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
        alipay_public_key_string=APP_PUBLIC_KEY_STRING,
        sign_type="RSA2",  # RSA 或者 RSA2
        debug = False  # 默认False
    )
    subject = '当前订单'

    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=order_id,
        total_amount=0.01,
        subject=subject,
        return_url="127.0.0.1:8000/axforder/pay_success/",
        notify_url="https://example.com/notify"  # 可选, 不填则使用默认notify url
    )

    return redirect('https://openapi.alipaydev.com/gateway.do?' + order_string)


def pay_success(request):
    return render(request,'axf/order/pay_success.html')