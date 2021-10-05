from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import AddTodoForm, ChangePasswordForm, LoginForm, SignupForm
from .models import addTodo
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import auth


# Function will show add todos and show all todos
def showTodo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            td = AddTodoForm(request.POST)
            if td.is_valid():
                ttl = td.cleaned_data['title']
                des = td.cleaned_data['description']
                reg = addTodo(title=ttl, description=des)
                reg.save()
                td = AddTodoForm()
        else:
            td = AddTodoForm()

        todoData = addTodo.objects.all()
        return render(request, "index.html", {'form': td, 'data': todoData})
    else:
        return HttpResponseRedirect('login')


# This will update todo
def updateTodo(request, id):
    if request.method == 'POST':
        pi = addTodo.objects.get(pk=id)
        td = AddTodoForm(request.POST, instance=pi)
        if td.is_valid():
            td.save()
    else:
        pi = addTodo.objects.get(pk=id)
        td = AddTodoForm(instance=pi)
    return render(request, "update.html", {'form': td})


# This will delete todo
def deleteTodo(request, id):
    if request.method == 'POST':
        pi = addTodo.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

def Signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('login')
        else:
            fm = SignupForm()
        context = {'form':fm}
        return render(request, 'signup.html', context)
    else:
        return HttpResponseRedirect('/')

def Login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    return HttpResponseRedirect('/')
        else:
            fm = LoginForm()
        context = {'form':fm}
        return render(request, 'login.html', context)
    else:
        return HttpResponseRedirect('/')

def Logout(request):
    logout(request)
    return HttpResponseRedirect('login')

def ChangePass(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = ChangePasswordForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                return HttpResponseRedirect('/')
        else:
            fm = ChangePasswordForm(user=request.user)
    else:
        return HttpResponseRedirect('login')
    context = {'form':fm}
    return render(request, 'changepass.html', context)