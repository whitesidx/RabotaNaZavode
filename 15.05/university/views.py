from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def courses(request):
    return render(request, "courses.html")

def teachers(request):
    return render(request, "teachers.html")

def contacts(request):
    return render(request, "contacts.html")
