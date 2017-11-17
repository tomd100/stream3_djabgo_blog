from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Post
from .forms import BlogPostForm

#-------------------------------------------------------------------------------

def list_posts(request):
    if request.user.is_authenticated():
        blog_title = "Blog Posts:"
        posts = Post.objects.filter(author=request.user);
    else:
        blog_title = "Blog Posts"
        posts = Post.objects.order_by('-published_date')
    return render(request, "list_posts.html", {'posts': posts, "blog_title": blog_title})    

#-------------------------------------------------------------------------------

def view_post(request, id):
    post = get_object_or_404(Post, pk=id);
    return render(request, "view_post.html", {"post": post});

#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def new_post(request):
    blog_title = "New Post:"
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False);
            post.author = request.user;
            post.published_date = timezone.now();
            post.save();
            return redirect(view_post, post.pk)
    else:
        form = BlogPostForm()
    return render(request, "edit_post.html", {"form":form, "blog_title": blog_title})

#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def edit_post(request, id):
    blog_title = "Edit Post:"
    post = get_object_or_404(Post, pk=id);
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit = False);
            post.author = request.user;
            post.published_date = timezone.now();
            post.save();
            return redirect(view_post, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, "edit_post.html", {"form":form, "blog_title": blog_title})

#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id);
    Post.objects.filter(id=post.id).delete()
    return redirect(list_posts)

#-------------------------------------------------------------------------------

    
