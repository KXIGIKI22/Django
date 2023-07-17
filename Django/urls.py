from django.urls import path
from myapp.views import my_users_view
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', my_users_view, name='home'),
    path('admin/', admin.site.urls),
    path('users/', my_users_view, name='users'),
]