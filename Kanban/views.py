from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from Kanban.script import check_for_mail, check_for_user
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from Kanban.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@require_http_methods(["POST"])
@csrf_exempt
def register_view(request):
    if check_for_user(request) and check_for_mail(request):
        User.objects.create_user(username=request.POST.get('userName', None),
                                 email=request.POST.get(
            'email', None),
            password=request.POST.get('password', None), first_name=request.POST.get('userName', None))
        return HttpResponse(status=200)
    else:
        return HttpResponse({'error2': 'user aready exists'})


@require_http_methods(["POST"])
@csrf_exempt
def login_view(request):
    user = authenticate(username=request.POST.get(
        'userName'), password=request.POST.get('password'))
    if user:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key})
    else:
        return HttpResponse(status=401)


def task_view(request):
    return HttpResponse({'test': 'test'})
# @api_view(['GET'])
# def current_user(request):
#     serializer = UserSerializer(request.user)
#     return HttpResponse(request.user)


# @api_view(['GET'])
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
