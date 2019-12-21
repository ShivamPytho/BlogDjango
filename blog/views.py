from django.shortcuts import render,HttpResponse
from blog.models import POST
# Create your views here.
def blogHome(request):
    allpost = POST.objects.all()
    context = {"allpost": allpost}
    return render(request, 'blog/bloghome.html', context)
    
def blogPost(request, slug):
    post = POST.objects.filter(slug=slug).first()
    context= {'post':post}
    return render(request, 'blog/blogpost.html', context)
    #return render(request, (f"blog/blogpost.html:{slug}"))
    