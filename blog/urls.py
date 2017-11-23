from django.conf.urls import url
from django.contrib import admin

from accounts.views import get_index
from blog.views import list_posts, view_post, new_post, edit_post, delete_post, add_comment

urlpatterns = [
    url(r"^$", list_posts, name="list_posts"),
    url(r"^new$", new_post, name="new_post"),
    url(r"^view/(\d+)$", view_post, name="view_post"),
    url(r"^edit/(\d+)$", edit_post, name="edit_post"),
    url(r"^delete/(\d+)$", delete_post, name="delete_post"),
    url(r"^(\d+)comment/add$", add_comment, name="add_comment"),
]

