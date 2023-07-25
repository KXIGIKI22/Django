import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django.settings')

django.setup()

from myapp.models import User

user = User.objects.create(id=1, name='Імʼя користувача', email='user@example.com', age=25)