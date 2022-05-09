from django.db import models
from django.contrib import admin

class User(models.Model):
    Name = models.CharField(max_length=100)
    Phone = models.IntegerField()
    Email = models.EmailField()
    City = models.CharField(max_length=100)

    def __str__(self):
        return self.Name


class User_admin(admin.ModelAdmin):
    list_display = ('Name', 'Phone', 'Email', 'City')