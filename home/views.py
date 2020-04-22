from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact, signUp
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User  #database me user signup ke liya import karo
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
    if len(query)>78:
        allpost = POST.objects.none()
    else:
        allposttitle = POST.objects.filter(title__icontains=query)
        allpostcontent = POST.objects.filter(content__icontains=query)
        allpost = allposttitle.union(allpostcontent)
    if allpost.count() == 0:
        messages.warning(request, "no search result found. please refine your query")
    params = {"allpost":allpost, "query":query}
    return render(request, 'home/search.html', params)

def signup(request):
     if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        print(username,fname,lname,email,password,password1)
         #check for error input

          #Create the User
        #myuser = User.objects.create(username=username, email=email, password=password)
        user = User(username=username,first_name=fname,last_name=lname,email=email,password=password)
        #myuser.first_name = fname
        #myuser.last_name = lname
        user.save()
        messages.success(request, "your account has been successful created")
        return redirect('home/home.html')
     return render(request, "404 - not found")

def hanidlLogin(request):
    if request.method == 'POST':
       loginusername = request.POST['loginusername']
       print(loginusername)
       loginpassword = request.POST['loginpassword']

       user1 = authenticate(username=loginusername, password=loginpassword)
       print(user1)
       if user1:
           login(request, user1)
           messages.success(request, "Successfully LogIn !!!")
           return redirect('home/home.html')
       else:
            messages.error(request, "invalid Username And Password !!! ")
            return redirect('home/home.html')
    return render(request, "404 - not found")
    

def hanidlLogout(request):
    logout(request)
    messages.success(request, "Successfully LogOut !!!")     
    return redirect('home/home.html')