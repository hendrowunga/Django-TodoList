from django.shortcuts import render,redirect
from .models import TodoForm
from .models import Todo



def home(request):
    todolist=Todo.objects.all()
    context={
        'todolist':todolist,
    }
    return render(request,'todoapp/home.html',context)

def add_todo(request):
    form=TodoForm()
    if request.method=='POST':
        FORM=TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
        context={
            'form':form
        }
        return render(request,'todoapp/todo_from.html',context)
        
        
        
        
        
        
        
        
        