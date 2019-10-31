from django.shortcuts import render,get_object_or_404
from blog.models import Blog
# Create your views here.

def blogs(request):
    bl = Blog.objects.all()
    return render(request,'blogs.html',{'bl':bl})
def detail(request,post_id):
    bl = get_object_or_404(Blog, pk=post_id)
    return render(request,'details.html',{'post':bl})
def cat(request,cat):
    bl = Blog.objects.filter(category=cat)
    return render(request,'cat.html',{'bl':bl})