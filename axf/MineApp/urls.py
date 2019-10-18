from django.conf.urls import url

from MineApp import views

urlpatterns = [
    url(r'^mine/',views.mine,name='mine'),
    #判断是否登录
    url(r'^logout/',views.logout,name='logout'),
]