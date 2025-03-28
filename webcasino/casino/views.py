from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from casino.models import CustomUser

User = get_user_model()

def home(request):
    return render(request, "casino/home.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        
        if password != password2:
            messages.error(request, 'Hasła muszą być takie same!')
            return redirect('register')

        
        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, 'Użytkownik o tej nazwie już istnieje!')
            return redirect('register')

        
        user = CustomUser.objects.create_user(username=username, password=password)
        
        
        user.saldo = 1000 
        user.save()
        
        messages.success(request, 'Rejestracja zakończona sukcesem!')
        return redirect('login')  

    return render(request, 'casino/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Zalogowano pomyślnie!')
            return redirect('home') 
        else:
            messages.error(request, 'Nieprawidłowa nazwa użytkownika lub hasło.')

    return render(request, 'casino/login.html')