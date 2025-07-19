# todo/urls.py

from django.urls import path
from .views import todo_list, add_todo, complete_todo, delete_todo

urlpatterns = [
    path('', todo_list, name='todo_list'),
    path('add/', add_todo, name='add_todo'),
    path('complete/<int:todo_id>/', complete_todo, name='complete_todo'),
    path('delete/<int:todo_id>/', delete_todo, name='delete_todo'),
]

