from django.shortcuts import render
from .models import Register


def index(request):
    return render(request, 'pages/index.html')

def list(request):
    new_user = Register()
    new_user.request.POST.get('name_user')
    new_user.request.POST.get('age_user')
    new_user.save()

    users = {
        'users': Register.objects.all()
    }

    return render(request, 'pages/list.html', users)