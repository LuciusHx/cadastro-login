from django.shortcuts import render
from usuarios.models import Usuario
from django.contrib import messages
# Create your views here.

def index(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname'),
        lastname = request.POST.get('lastname'),
        email = request.POST.get('email'),
        number = request.POST.get('number'),
        password = request.POST.get('password'),     
        password2 = request.POST.get('confirmPassword'),
    
        if password != password2:
            messages.error(request, "Passwords do not match")
            return render(request, 'index.html')
        
        new_user = Usuario(
            firstname=firstname,
            lastname=lastname,
            email=email,
            number=number,
            password=password
        )
        new_user.save()
        return render(request, 'listagem_usuarios.html')
       
    return render(request, 'index.html')
    

def login(request):
    return render(request, 'login.html')

def listagem_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'listagem_usuarios.html', {'usuarios': usuarios})