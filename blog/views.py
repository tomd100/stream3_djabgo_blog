from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

from .models import Post, Comment
from .forms import BlogPostForm, BlogCommentForm

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

# def view_post(request, id):
#     post = get_object_or_404(Post, pk=id);
#     return render(request, "view_post.html", {"post": post});
    
def view_post(request, id):
    this_post = get_object_or_404(Post, pk=id)
    comments = Comment.objects.filter(post = this_post);
    form = BlogCommentForm()
    return render(request, "view_post.html", {"post": this_post, "comments": comments, "form": form})

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
    
    # if post.id in Post.objects.all().filter(post.user = Post.user):
    #     Post.objects.filter(id=post.id).delete()                                # is there a command to commit to the database?
    # else:
        # messages.error(request, "Error")
    
    Post.objects.filter(id=post.id).delete()
    return redirect(list_posts)                                                 # how to make sure that the delte only happens for the right id. 
                                                                                # there are issues with the flow - going back a page allows delete of other users blog
#-------------------------------------------------------------------------------

@login_required(login_url="/accounts/login")
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id);
    form = BlogCommentForm(request.POST);
    if form.is_valid():
        comment = form.save(commit = False);
        
        comment.author = request.user
        comment.post = post
        
        comment.save()
        
        return redirect('view_post', post_id)

#-------------------------------------------------------------------------------