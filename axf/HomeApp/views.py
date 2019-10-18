from django.shortcuts import render

# Create your views here.
from HomeApp.models import Axf_wheel, Axf_nav, Axf_mustbuy, Axf_mainshow


def home(request):
    wheels = Axf_wheel.objects.all()
    navs = Axf_nav.objects.all()
    mustbuys = Axf_mustbuy.objects.all()
    mainshows = Axf_mainshow.objects.all()
    context = {
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'mainshows':mainshows,
    }

    return render(request, 'axf/main/home/home.html',context=context)


