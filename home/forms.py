from django import forms
from django.forms import fields, widgets
from .models import addTodo

class AddTodoForm(forms.ModelForm):
    class Meta:
        model = addTodo
        fields = ['title', 'description']
        widgets = {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
        }