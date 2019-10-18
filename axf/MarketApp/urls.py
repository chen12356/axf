from django.conf.urls import url

from MarketApp import views

urlpatterns = [
    url(r'^market/',views.market,name='market'),
    url(r'^addTocart/', views.addTocart, name='addTocart'),
    url(r'^subTocart/', views.subTocart, name='subTocart'),

]