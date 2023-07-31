from django.urls import path
from .views import UserListView, UserDetailView, CreateUserView

urlpatterns = [
    path('', UserListView.as_view(), name='user_list'),  # URL для списку користувачів
    path('create/', CreateUserView.as_view(), name='user_create'),  # URL для створення користувача
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),  # URL для деталей користувача
]