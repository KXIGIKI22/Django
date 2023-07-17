from django.http import HttpResponse

def my_users_view(request):
    return HttpResponse("Hello, users!")

def users_view(request):
    return HttpResponse("Hello, admin users!")
