from django.shortcuts import render

def home(request):
    return render(request, "u_registeration/home.html")
def register(request):
    return render(request, "u_registeration/register.html")
def login(request):
    return render(request, "u_registeration/login.html")

# Create your views here.
