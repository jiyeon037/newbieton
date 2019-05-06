from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm

def home(request):
    return render(request, "r_registeration/home.html")

def roomregister(request):
     return render(request, "r_registeration/roomregister.html")
    
def find(request):
    blog = Blog.objects
    return render(request, "r_registeration/find.html", {'blog' : blog})

def detail(request,blog_id):
    blog_detail = get_object_or_404(Blog, pk = blog_id)
    return render(request, "r_registeration/detail.html", {'blog' : blog_detail})

def postcreate(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('home')
    else:
        form = BlogForm()
        return render(request, 'r_registeration/roomregister.html', {'form':form})
