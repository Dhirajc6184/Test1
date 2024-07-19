from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def login (request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        print(username,password)
        user=auth.authenticate(username=username,password=password)
    
        if user.is_staff:
            print('true staff')
            return redirect('home')
        else:
            return redirect('signup')

            
            return redirect('home')

        
    return render (request,'login.html')

def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        email=request.POST['email']
        name=request.POST['fullname']
        print(username,password,email,name)



        user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
                first_name=name
            )
        user.save()
    return render (request,'signup.html')

def home(request):
    return render (request,'home.html')