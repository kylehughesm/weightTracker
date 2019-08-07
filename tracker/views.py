from django.shortcuts import render, redirect
from tracker.models import Entry
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, models
from django.contrib import messages


def home(request):
    if request.user.is_authenticated:
        user = request.user
    else:
        user = None
    return render(request, 'tracker/home.html', {'user': user})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('/')
        else:
            return render(request, 'tracker/register.html', {'form': form})
    form = UserCreationForm()
    return render(request, 'tracker/register.html', {'form': form})


def login_user(request):
    return redirect('/accounts')


def profile(request):
    return render(request, 'tracker/profile.html')


def enter_weight(request):
    if request.method == 'POST':
        scale = request.POST['entry_weight']
        Entry.objects.create(weight=scale)
        return redirect('history')
    return render(request, 'tracker/enter.html')


def history(request):
    entries = Entry.objects.all()
    history = {'entries': entries}
    return render(request, 'tracker/history.html', history)
