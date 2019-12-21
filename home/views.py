from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages
from blog.models import POST
# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST ['name']
        email = request.POST ['email']
        phone = request.POST ['phone']
        describe = request.POST ['describe']
       #print(name, email, phone, describe)
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(describe)<4:
            messages.error(request, "please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, content=describe)
            contact.save()
            messages.success(request, "your message has been successfuly Sent")
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET['query']
    allpost = POST.objects.filter(title__icontains=query)
    params = {"allpost":allpost, "query":query}
    return render(request, 'home/search.html', params)