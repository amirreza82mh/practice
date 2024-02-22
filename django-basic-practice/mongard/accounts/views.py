from django.shortcuts import render, redirect
from .forms import RegisterUserForm, LoginUserForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required


def user_register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            user = User.objects.create_user(username=info['username'], email=info['email'], password=info['password'])
            user.first_name = info['first_name']
            user.last_name = info['last_name']
            user.save()
            messages.success(request, 'user registered successfully', extra_tags='success')
            return redirect('home')

    else:
        form = RegisterUserForm()

    context = {
        'form': form,
    }

    return render(request, 'register.html', context=context)


def user_login(request):
    if request.method == "POST":
        form = LoginUserForm(request.POST)

        if form.is_valid():
            info = form.cleaned_data
            user = authenticate(request, username=info['username'], password=info['password'])

            if user is not None:
                login(request, user)
                messages.success(request, 'login successfully', extra_tags='success')
                return redirect('home')

            else:
                messages.error(request, 'username or password is not valid', extra_tags='danger')

    else:
        form = LoginUserForm()

    context = {
        'form': form,
    }

    return render(request, 'login.html', context=context)


@login_required(login_url='user_login')
def user_logout(request):
    logout(request)
    messages.success(request, 'user logged out successfully!', extra_tags='warning')
    return redirect('home')
