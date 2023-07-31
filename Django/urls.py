#from django.urls import path
#from myapp.views import my_users_view
#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('users/', include('user.urls')),
#    path('books/', include('book.urls')),
#    path('purchases/', include('purchase.urls')),
#]
from django.urls import path
from .views import UserListView, UserDetailView, PurchaseListView, PurchaseDetailView, BookListView, BookDetailView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
    path('users/create/', CreateUserView.as_view(), name='user_create'),
    path('purchases/', PurchaseListView.as_view(), name='purchase_list'),
    path('purchases/<int:pk>/', PurchaseDetailView.as_view(), name='purchase_detail'),
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('admin/', admin.site.urls),
    path('api/', include('Django22.api.urls')),
]