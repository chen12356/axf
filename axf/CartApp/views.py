from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

from CartApp.models import Axf_cart
from MarketApp.models import Axf_goods


def cart(request):
    # user_id = request.session.get('user_id')
    # if user_id:
        user = request.user  #中间进行处理了
        print(user.id)
        carts = Axf_cart.objects.filter(c_user_id=user.id)
        if carts.count()>0:
            # 用于判断是否存在选中的，返回没选的，然后在exists得到选中的，在not取反
            # 假设找到一个false，在exists,得到True，然后在not 又是false
            #全部都是false，在exists,得到true，用
            #没有false，那么直接用exists找不到 返回false，not就为true

            is_all_select = not Axf_cart.objects.filter(c_is_select=False).exists()
            print(is_all_select)
            context = {
                'carts':carts,
                'total_price':total_price(user.id),
                'user_id':user.id,
                'is_all_select':is_all_select,
            }
            # print(goods_num_list)
        else:
            context = {
                'total_price':total_price(user.id),
                'is_all_select': False,
            }
        return render(request,'axf/main/cart/cart.html',context=context)
    # return redirect(reverse('axfuser:login'))

def total_price(user_id):
    carts = Axf_cart.objects.filter(c_user_id=user_id)
    total_price = 0
    for cart in carts:
        print('xxxxxxxxxxxxxxxxxxx')
        print(cart.c_goods_num)
        if cart.c_is_select:
            total_price = total_price + cart.c_goods_num * cart.c_goods.marketprice
    print(total_price)
    return  '%.2f'%total_price

@csrf_exempt
def subShopping(request):
    # 实现购物车商品的数量减少
    # goodsid = request.GET.get('goodsid')
    cartid = request.POST.get('cartid')
    print(cartid)
    cart = Axf_cart.objects.get(pk=cartid)

    data = {
        'msg':'ok',
        'status':200,
    }
    if cart.c_goods_num == 1:
        cart.delete()

        data['status'] = 201

    else:
        cart.c_goods_num = cart.c_goods_num -1
        cart.save()
        data['c_goods_num'] = cart.c_goods_num
    # user_id = request.session.get('user_id')
    user = request.user
    print('================')
    print(user.id)
    print(total_price(user.id))
    data['total_price'] = total_price(user.id)
    print('------------')
    print(data['total_price'] )
    return JsonResponse(data=data)


def changeStatus(request):
    data = {
        'msg':'ok',
        'status':200,
    }
    cartid = request.GET.get('cartid')
    cart = Axf_cart.objects.get(pk=cartid)
    cart.c_is_select = not cart.c_is_select
    cart.save()

    data['c_is_select'] = cart.c_is_select
    # user_id = request.session.get('user_id')
    user = request.user
    print(total_price(user.id))
    data['total_price'] = total_price(user.id)

    # 也需要判断下是不是全部都选了，或者存在没选的
    is_all_select = not Axf_cart.objects.filter(c_is_select=False).exists()
    data['is_all_select'] = is_all_select

    return JsonResponse(data=data)


# def all_status(request):
#     data = {
#         'msg':'ok',
#         'status':200,
#     }
#     info = request.GET.get('info')
#     user_id = request.session.get('user_id')
#     carts = Axf_cart.objects.filter(c_user_id=user_id)
#     for cart in carts:
#         if info == '0':
#             cart.c_is_select = 1
#             data['c_is_select'] = True
#         else:
#             cart.c_is_select = 0
#             data['c_is_select'] = False
#         cart.save()
#     return JsonResponse(data=data)
def all_select(request):
    data = {
            'msg':'ok',
            'status':200,
        }
    cart_str = request.GET.get('cartid_str')
    carids = cart_str.split('#')
    # 找到这个列表的id对象，把选中状态取反
    cart_list = Axf_cart.objects.filter(id__in = carids)
    for cart in cart_list:
        cart.c_is_select = not cart.c_is_select
        cart.save()
    # user_id = request.session.get('user_id')
    user = request.user
    print(user.id)
    data['total_price'] = total_price(user.id)
    return  JsonResponse(data=data)