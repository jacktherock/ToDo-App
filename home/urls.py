
from django.urls import path
from . import views

urlpatterns = [
    path('', views.showTodo, name="showtodo"),
    path('update/<int:id>/', views.updateTodo, name="updatetodo"),
    path('delete/<int:id>/', views.deleteTodo, name="deletetodo"),
    path('signup', views.Signup, name="signup"),
    path('login', views.Login, name="login"),
    path('logout', views.Logout, name="logout"),
    path('changepass', views.ChangePass, name="changepass"),
]
