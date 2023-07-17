from django.http import HttpResponse

def users_view(request):
    return HttpResponse("Hello, users!")

def admin_users_view(request):
    return HttpResponse("Hello, admin users!")