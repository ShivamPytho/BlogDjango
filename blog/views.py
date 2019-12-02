from django.shortcuts import render,HttpResponse

# Create your views here.
def blogHome(request):
    return HttpResponse("This is blogHome: We Will be keep all the posts here")

def blogPost(request, slug):
    return HttpResponse(f" blogPost:{slug}")