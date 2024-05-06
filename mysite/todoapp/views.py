from django.shortcuts import get_object_or_404, render, redirect
from .forms import TodoForm
from .models import Todo

def home(request):
    todolist = Todo.objects.all()
    context = {
        'todolist': todolist,
    }
    return render(request, 'todoapp/home.html', context)

def add_todo(request):
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    # Render form jika metode request bukan POST atau form tidak valid
    context = {
        'form': form
    }
    return render(request, 'todoapp/todo_form.html', context)

def update_todo(request,pk):
    item=get_object_or_404(Todo,id=pk)
    form=TodoForm(instance=item)
    if request.method=='POST':
        form=TodoForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    context={
        'form':form
    }
    return render(request,'todoapp/todo_form.html',context)


def delete_todo(request,pk):
    item=get_object_or_404(Todo,id=pk)
    context= {
        'item':item,
    }
    return render(request,'todoapp/delete_todo.html',context)

def accept_delete_todo(request,pk):
    todo=get_object_or_404(Todo,id=pk)
    todo.delete()
    return redirect('home')
