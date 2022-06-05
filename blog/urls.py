# blog/urls.py
from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
        path('post/<int:pk>/', BlogDetailView.as_view(),
            name='post_detail'), # creates a url for each individual blog post
        path('', BlogListView.as_view(), name='home'), # make a url named 'home'
        ]
