from django.urls import path
from myapp.views import my_users_view
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('user.urls')),  # Включаємо URL-адреси додатку "user"
    path('books/', include('book.urls')),
    path('purchases/', include('purchase.urls')),
]