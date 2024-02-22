from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import CreateTodoForm, UpdateTodoForm


def say_hello(request):
    person = {
        'first_name': 'Amirreza',
        'last_name': 'Mehrabani',
    }

    return render(request, 'hello.html', context=person)


def home(request):
    all = Todo.objects.all()

    context = {
        'all': all,
    }

    return render(request, 'home.html', context=context)


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    context = {
        'todo': todo
    }

    return render(request, 'detail.html', context=context)


def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    messages.success(request, 'Todo deleted successfully', extra_tags='success')

    return redirect('home')


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)

    if request.method == "POST":
        form = UpdateTodoForm(request.POST, instance=todo)

        if form.is_valid():
            form.save()
            messages.success(request, 'your Todo updated successfully', extra_tags='success')
            return redirect('detail', todo_id)

    else:
        form = UpdateTodoForm(instance=todo)

    context = {
        'form': form,
    }

    return render(request, 'update.html', context=context)


def create(request):
    if request.method == "POST":
        form = CreateTodoForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            Todo.objects.create(title = info['title'], body = info['body'], created = info['created'])
            messages.success(request, 'Todo is created successfully', extra_tags='success')
            return redirect('home')

    else:
        form = CreateTodoForm()

    context = {
        'form': form,
    }

    return render(request, 'create.html', context=context)
