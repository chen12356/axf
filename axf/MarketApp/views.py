from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from CartApp.models import Axf_cart
from MarketApp.models import Axf_foodtype, Axf_goods
from MarketApp.view_helper import ORDER_RULE_DEFAULT, ORDER_RULE_NUM_ASC, ORDER_RULE_NUM_DESC, ORDER_RULE_PRICE_ASC, \
    ORDER_RULE_PRICE_DESC


def market(request):
    axf_foodtypes = Axf_foodtype.objects.all()
    typeid = request.GET.get('typeid', '104749')
    childtypenames = Axf_foodtype.objects.filter(typeid=typeid)[0]
    childtypenames_list = childtypenames.childtypenames.split("#")
    typenames_list = []
    sort_type_list = [['综合排序', ORDER_RULE_DEFAULT],
                      ['销量升序', ORDER_RULE_NUM_ASC],
                      ['销量降序', ORDER_RULE_NUM_DESC],
                      ['价格升序', ORDER_RULE_PRICE_ASC],
                      ['价格降序', ORDER_RULE_PRICE_DESC]]
    for typenames in childtypenames_list:
        name = typenames.split(":")
        typenames_list.append(name)
        # print(typenames_list)

    childcid = request.GET.get('childcid', '0')
    sort_type = request.GET.get('sort_type', '0')
    axf_goods = Axf_goods.objects.filter(categoryid=typeid)

    # if childcid:
    if childcid == '0':
        pass
    else:
        axf_goods = axf_goods.filter(childcid=childcid)
        # if sort_type == '0':
        #     axf_goods = axf_goods
        # if sort_type == 'desc_productnum':
        #     axf_goods = axf_goods.order_by('-productnum')
        # if sort_type == 'productnum':
        #     axf_goods = axf_goods.order_by('productnum')
        # if sort_type == 'price':
        #     axf_goods = axf_goods.order_by('price')
        # if sort_type == 'desc_price':
        #     axf_goods = axf_goods.order_by('-price')
    # else:
        #     axf_goods = axf_goods.filter(childcid=childcid)

    if sort_type == ORDER_RULE_DEFAULT:
            axf_goods = axf_goods
    if sort_type == ORDER_RULE_NUM_DESC:
            axf_goods = axf_goods.order_by('-productnum')
    if sort_type == ORDER_RULE_NUM_ASC:
            axf_goods = axf_goods.order_by('productnum')
    if sort_type == ORDER_RULE_PRICE_ASC:
            axf_goods = axf_goods.order_by('marketprice')
    if sort_type == ORDER_RULE_PRICE_DESC:
            axf_goods = axf_goods.order_by('-marketprice')

    context = {
        'axf_foodtypes': axf_foodtypes,
        'axf_goods': axf_goods,
        'typeid': typeid,
        'childcid': childcid,
        'sort_type': sort_type,
        'typenames_list': typenames_list,
        'sort_type_list': sort_type_list,
    }
    return render(request, 'axf/main/market/market.html', context=context)

def addTocart(request):
    # user_id = request.session.get('user_id')
        user = request.user
        data = {
            'msg':'ok',
            'status':200,
        }
    # if user_id:
        goodsid = request.GET.get('goodsid')
        print('------------------')
        print(goodsid)
        carts = Axf_cart.objects.filter(c_user_id=user.id).filter(c_goods_id=goodsid)
        if carts.count() > 0:
            cart = carts.first()
            cart.c_goods_num = cart.c_goods_num + 1
        else:
            cart = Axf_cart()
            cart.c_goods_id = goodsid
            cart.c_user_id = user.id
        cart.save()
        data['c_goods_num'] = cart.c_goods_num
        return JsonResponse(data=data)
    # else:
    #     data['msg'] = '用户没有登录'
    #     data['status'] = 201
    #     return JsonResponse(data=data)


def subTocart(request):
    # user_id = request.session.get('user_id')
        user = request.user
        data = {
            'msg': 'ok',
            'status': 200,
        }
    #
    # if user_id:
        goodsid = request.GET.get('goodsid')
        carts = Axf_cart.objects.filter(c_user_id=user.id).filter(c_goods_id=goodsid)
        if carts.count() > 0:
            cart = carts.first()
            if cart.c_goods_num == 1:
                # cart.c_goods_num = cart.c_goods_num - 1
                # cart.save()
                data['c_goods_num'] = 0
                cart.delete()
            else:
                cart.c_goods_num = cart.c_goods_num - 1
                cart.save()
                data['c_goods_num'] = cart.c_goods_num
        # else:
        #
        return JsonResponse(data=data)
    # else:
    #     data['msg'] = '用户没有登录'
    #     data['status'] = 201
    #     return JsonResponse(data=data)
