from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .forms import AddTodoForm
from .models import addTodo


# Function will show add todos and show all todos
def showTodo(request):
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
