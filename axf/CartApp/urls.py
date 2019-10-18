from django.conf.urls import url

from CartApp import views

urlpatterns = [
    url(r'^cart/',views.cart,name='cart'),
#     减少商品
    url(r'^subShopping/',views.subShopping,name='subShopping'),
    url(r'^changeStatus/',views.changeStatus,name='changeStatus'),
    url(r'^all_select/',views.all_select,name='all_status'),
]