from django.shortcuts import render
from django.views import View
from .models import User
from .forms import UserForm

class UserListView(View):
    def get(self, request):
        users = User.objects.all()
        return render(request, 'user_list.html', {'object_list': users})

class UserDetailView(View):
    def get(self, request, id, pk):
        user = User.objects.get(pk=id)
        return render(request, 'user_detail.html', {'user': user})

class CreateUserView(View):
    def get(self, request):
        form = UserForm()
        return render(request, 'create_user.html', {'form': form})

    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
        return render(request, 'create_user.html', {'form': form})