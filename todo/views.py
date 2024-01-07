from django.shortcuts import render,redirect
from .models import Todolist

# Create your views here.
def index(request):
    if request.POST:
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
        return redirect('index')
    todo_items = Todolist.objects.order_by('id')
    context = {'todo_items':todo_items}
    return render(request,'index.html',context)

def completedTodo(request, todo_id)  :  
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = True
    todo.save()
    return redirect('index')
    
def uncomplete(request, todo_id)  :  
    todo = Todolist.objects.get(pk=todo_id)
    todo.completed = False
    todo.save()
    return redirect('index')

def deleteCompleted(request):
    Todolist.objects.filter(completed__exact=True).delete()
    return redirect('index')

def deleteAll(request):
    Todolist.objects.all().delete()
    return redirect('index')
