from django.urls import path
from . import views

urlpatterns = [
    path("blogposts/", views.BlogPostList.as_view(), name="blogpost-view-create"),
]