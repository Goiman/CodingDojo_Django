from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'first_app/index.html')

def succes(request):

    context = {
        'first_name': request.POST['first_name'],
        'last_name': request.POST['last_name'],
        'email': request.POST['email'],
        'password': request.POST['password'],
        'password_confirmation': request.POST['password_confirmation'],    
    }
    return render(request,'first_app/succes.html', context)
