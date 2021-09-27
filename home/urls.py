
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showTodo, name="showtodo"),
    path('update/<int:id>/', views.updateTodo, name="updatetodo"),
    path('delete/<int:id>/', views.deleteTodo, name="deletetodo"),
]
