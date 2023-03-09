from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from Kanban.views import register_view, login_view, UserViewSet, task_view
from rest_framework.authtoken import views


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
# router.register(r'todos', TodoViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register/', register_view),
    path('login/', login_view),
    path(r'api-token-auth/', views.obtain_auth_token),
    path('task/', task_view)
]
