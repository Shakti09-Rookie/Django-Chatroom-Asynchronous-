from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def room(request, room_name):
    return render(request, 'chatroom.html', {
        'room_name': room_name
    })

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ('Registration Successful'))
            return redirect('login')
    else:
        form = UserCreationForm

    context = {'form' : form}
    return render(request, 'registration/register.html', context)