from django.http import JsonResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin

# 存放获取请求的路由,哪些路由的视图函数需要用到，都加这个列表中
from UserApp.models import Axf_user

LOGIN_REQUEST = ['/axfcart/cart/',]
#存放请求的路由并且返回json数据
LOGIN_REQUEST_JSON = ['/axfmarket/addTocart/',
                      '/axfmarket/subTocart/',
                      '/axfcart/subShopping/',
                      '/axfcart/all_select/',
                      '/axfcart/changeStatus/',]
# 由于每次都要获取user_id，直接利用中间件来处理。
class LoginMiddleware(MiddlewareMixin):
    # 在路由分发前先执行的操作(在执行视图函数之前)
    def process_request(self,request):
        # 获取user_id
        user_id = request.session.get('user_id')
        if request.path in LOGIN_REQUEST:
            if user_id:
                user = Axf_user.objects.get(pk=user_id)
                # 给request设置属性为user对象，可以在任何地方使用，非常牛x
                request.user = user
            else:
                # 跳转登录
                return  redirect(reverse('axfuser:login'))
        if request.path in LOGIN_REQUEST_JSON:
            if user_id:
                user = Axf_user.objects.get(pk=user_id)
                # 给request设置属性为user对象，可以在任何地方使用，非常牛x
                request.user = user
            else:
                data = {}
                data['msg'] = '用户没有登录'
                data['status'] = 201
                return JsonResponse(data=data)