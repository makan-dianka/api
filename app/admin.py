from django.contrib import admin

from .models import User, User_admin
admin.site.register(User, User_admin) 
