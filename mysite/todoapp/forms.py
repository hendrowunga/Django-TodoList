from django import forms
from .models import Todo


class TodoForm(forms.ModelForms):
    class Meta:
        model=Todo
        field= ['title']
