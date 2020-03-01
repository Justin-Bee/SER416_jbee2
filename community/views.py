from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import *


@csrf_exempt
def database(request):
    response_data = {}
    if request.POST.get('action') == 'post':
        uname = request.POST.get('username')
        psword = request.POST.get('password')
        eml = request.POST.get('email')

        if User.objects.filter(username=uname, email=eml).exists():
            response = "FalseU"
            response_data['login'] = 'FalseU'
        elif User.objects.filter(email=eml).exists():
            response = "FalseE"
            response_data['login'] = 'FalseE'
        else:
            User.objects.create(
                username=uname,
                password=psword,
                email=eml,
            )
            response = "True"
            response_data['login'] = 'True'
    elif request.POST.get('action') == 'equipment':
        equip = Equipment.objects.all()
        type = request.POST.get('type')
        quantity = request.POST.get('quantity')

        if Equipment.objects.filter(type = type).exists():
            temp = Equipment.objects.get(type=type).quantity
            Equipment.objects.update(
                type = type,
                quantity = int(temp) + int(quantity)
            )
            response_data['equipment'] = 'True'
        else:
            Equipment.objects.create(
                type = type,
                quantity = quantity
            )
            response_data['equipment'] = 'True'

    return JsonResponse(equip)
