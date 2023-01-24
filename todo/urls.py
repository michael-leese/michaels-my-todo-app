from django.urls import path, include
from todo import views

urlpatterns = [
    path('', views.get_todo_list, name="todo_list"),
    path('add', views.add_item, name="add_item"),
    path('edit/<item_id>', views.edit_item, name="edit_item"),
    path('toggle/<item_id>', views.toggle_item, name="toggle_item"),
    path('delete/<item_id>', views.delete_item, name="delete_item"),
]