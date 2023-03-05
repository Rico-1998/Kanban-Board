from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from Kanban.script import check_for_mail, check_for_user


@csrf_exempt
def register_view(request):
    # if (request.method == 'POST'):
    #     User.objects.create_user(first_name=request.POST.get(
    #         'userName', None), email=request.POST.get('email', None), password=request.POST.get('password', None), username=request.POST.get('userName', None))
    # return JsonResponse({'test': 'ein test'})

    if check_for_user(request) and check_for_mail(request):
        User.objects.create_user(username=request.POST.get('userName', None),
                                 email=request.POST.get(
            'email', None),
            password=request.POST.get('password', None), first_name=request.POST.get('userName', None))
        return HttpResponse(status=200)
    else:
        return HttpResponse({'error2': 'user aready exists'})


@csrf_exempt
def login_view(request):
    user = authenticate(username=request.POST.get(
        'userName'), password=request.POST.get('password'))
    if user:
        login(request, user)
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=401)
