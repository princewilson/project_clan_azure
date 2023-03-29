from django.shortcuts import render
from django.contrib import messages
def base(request):
    msgs = messages.get_messages(request)
    data = {
        'messages' : msgs
    }
    return render(request, './base.html', data)