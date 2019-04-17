from django.shortcuts import render, redirect
from tracker.models import Entry


def home(request):
    return render(request, 'tracker/home.html')


def register(request):
    return render(request, 'tracker/register.html')


def login_user(request):
    return redirect('/user_account')


def logout_user(request):
    return redirect('/')


def login_page(request):
    return render(request, 'tracker/login.html')


def user_account(request):
    return render(request, 'tracker/account.html')


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
