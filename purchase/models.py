from django.db import models
from user.models import User
from book.models import Book

class Purchase(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField()

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.user.name} purchased {self.book.title} on {self.date}'