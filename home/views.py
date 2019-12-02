from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This Is home Page")

def about(request):
    return HttpResponse("This is about page")

def contact(request):
    return HttpResponse("this is contact page")