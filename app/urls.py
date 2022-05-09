from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('user/new', views.post, name="post"),
    path('user/<int:id>', views.show, name="show"),
    path('user/<int:id>/edit', views.edit, name="edit"),
    path('user/<int:id>/remove', views.remove, name="remove"),
]