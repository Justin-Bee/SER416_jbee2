from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from .models import User


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

    return JsonResponse(response_data)
