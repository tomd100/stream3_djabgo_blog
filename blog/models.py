from django.db import models
from django.utils import timezone


class Post(models.Model):  # why doe we not use class meta here?
    """  
    Here we'll define our Post model
    """
    
    # author is linked to a registered
    # user in the 'auth_user' table.
    
    author = models.ForeignKey('auth.User')  # why is this auth.User - where does the auth. part come from
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title
        
    def __str__(self):    # why does this work and the one above not. Also why, when adding this its effect was immediate without a migrate?
        return self.title    
        
class Comment(models.Model):
    author = models.ForeignKey('auth.User')  # why is this auth.User - where does the auth. part come from
    post = models.ForeignKey(Post, related_name = "comments")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(blank=False, default=False)
    
    def __str__(self):
        return self.title