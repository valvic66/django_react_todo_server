from django.urls import path
from . import views

urlpatterns = [
    path("", views.apiOverview, name="api-overview"),
    path("todo_create/", views.todoCreate, name="todo-create"),
    path("todo_list/", views.todoList, name="todo-list"),
    path("todo_update/<int:pk>/", views.todoUpdate, name="todo-update"),
    path("todo_delete/<int:pk>/", views.todoDelete, name="todo-delete"),
    path("todo_detail/<int:pk>/", views.todoDetail, name="todo-detail"),

    path("<int:id>/", views.detail, name="detail"),
    path("todo_lists/", views.todo_lists, name="todo_lists"), 
]