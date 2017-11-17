from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post


# @login_required(login_url="/accounts/login")
def posts(request):
    if request.user.is_authenticated():
        blog_title = "Blog Posts:"
        posts = Post.objects.filter(author=request.user);
    else:
        blog_title = ""
        posts=[];
    return render(request, "main.html", {'posts': posts, "blog_title": blog_title})    

def view_post(request, id):
    post = get_object_or_404(Post, pk=id);
    return render(request, "view_post.html", {"post": post});
    
    