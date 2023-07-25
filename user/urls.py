from django.urls import path
from .views import UserListView, UserDetailView, CreateUserView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:id>/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('create/', CreateUserView.as_view(), name='user_create'),
]