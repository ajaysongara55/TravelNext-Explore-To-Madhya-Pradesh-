from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render
from .models import Contact
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request,"index.html")

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        obj=Contact()
        obj.name=name
        obj.email=email
        obj.subject=subject
        obj.message=message
        obj.save()
        return render(request,'index.html')
    else:
        return render(request,"Contact.html")

def login(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        password = request.POST.get("password") 

        user = authenticate(request, username=fullname, password=password)

        if user is not None:
            auth_login(request, user)
            return render(request, "index.html")
        else:
            return render(request, "index.html", {'error': 'Invalid username or password.'})

    return render(request, "login.html")
    
def registration(request):
    if request.method=='POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=User.objects.create_user(username=fullname,email=email,password=password)
        user.save()
        return render(request,'login.html')
    else:
        return render(request,"registration.html")

def about(request):
    return render(request,"about.html")

def traveler(request):
    return render(request,"traveler.html")

def home(request):
    return render(request,"home.html")


def locations(request):
    return render(request,"locations.html")


def Ujjain(request):
    return render(request,"Ujjain.html")


def Indore(request):
    return render(request,"Indore.html")


def Bhopal(request):
    return render(request,"Bhopal.html")


def Pachmarhi(request):
    return render(request,"Pachmarhi.html")

def Omkareshwar(request):
    return render(request,"Omkareshwar.html")

def Jabalpur(request):
    return render(request,"Jabalpur.html")

def Vidisha(request):
    return render(request,"Vidisha.html")

def Khajuraho(request):
    return render(request,"Khajuraho.html")

def Kuno(request):
    return render(request,"Kuno.html")

def Rewa(request):
    return render(request,"Rewa.html")

def Shahdol(request):
    return render(request,"Shahdol.html")

def Mandsaur(request):
    return render(request,"Mandsaur.html")

def Gwalior(request):
    return render(request,"Gwalior.html")

def hotel(request):
    return render(request,"hotel.html")

def hotel(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        checkin=request.POST['checkin']
        checkout=request.POST['checkout']
        room=request.POST['room']
        notes=request.POST['notes']
        obj=hotel()
        obj.name=name
        obj.email=email
        obj.checkin=checkin
        obj.checkout=checkout
        obj.room=room
        obj.notes=notes
        obj.save()
        return render(request,'index.html')
    else:
        return render(request,"hotel.html")