from home.models import addTodo
from django.contrib import admin

# Register your models here.
@admin.register(addTodo)
class addTodoAdmin(admin.ModelAdmin):
    list_display=['id','title','description','date']