from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User

@login_required
def index(request):
    users = User.objects.exclude(id=request.user.id)
    return render(request, 'chat/index.html', {'users': users})

@login_required
def start_chat(request, receiver_id):
    receiver = User.objects.get(id=receiver_id)
    messages = ChatMessage.objects.filter(sender=request.user, receiver=receiver) | ChatMessage.objects.filter(sender=receiver, receiver=request.user)
    messages = messages.order_by('timestamp')
    room_name = f"{min(request.user.id, receiver.id)}_{max(request.user.id, receiver.id)}"
    return render(request, 'chat/chat.html', {'receiver': receiver, 'messages': messages, 'room_name': room_name})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'chat/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'chat/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')