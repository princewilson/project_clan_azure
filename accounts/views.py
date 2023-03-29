from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from post_content.models import Post

# Create your views here.
def signup(request):
    return render(request, './accounts/signup.html')

def callback(request):
    if request.user.is_authenticated:
        messages.add_message(request, messages.SUCCESS, f"Welcome, {request.user.first_name}. You have logged in successfully.")
        msgs = messages.get_messages(request)
        posts = Post.objects.all()
        data = {
            'messages' : msgs,
            'posts' : posts,
        }
        return render(request, './accounts/dashboard.html', data)
    return render(request, './base.html')

def logout_user(request):
    messages.add_message(request, messages.INFO, "You have logged out successfully.")
    logout(request)
    return redirect('base')