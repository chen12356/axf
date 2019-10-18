from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from UserApp.models import Axf_user


def mine(request):
    user_id = request.session.get('user_id')
    context ={}
    if user_id:
        user = Axf_user.objects.get(pk=user_id)
        context = {
            'user_id':user_id,
            'user':user,
        }
    return render(request,'axf/main/mine/mine.html',context=context)


def logout(request):
    request.session.flush()
    return redirect(reverse('axfmine:mine'))