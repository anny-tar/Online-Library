from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.ImageField(upload_to='covers/', null=True, blank=True)
    description = models.TextField()
    genres = models.JSONField(default=list)  # Хранение жанров в виде списка
    available_count = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    published_year = models.PositiveIntegerField(null=True, blank=True)
    created_year = models.PositiveIntegerField(null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    translator = models.CharField(max_length=255, null=True, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    booked_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_returned = models.BooleanField(default=False)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)