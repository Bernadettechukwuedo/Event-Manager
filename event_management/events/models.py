from django.db import models
from accounts.models import CustomUser


# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=250)
    capacity = models.IntegerField()
    organizer = models.CharField(max_length=250)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.title} created by {self.created_by.username} organized by {self.organizer} date: {self.date} time:{self.time}"
