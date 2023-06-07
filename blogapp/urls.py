from django.urls import path
from .views import BlogListView



urlpatterns = [
    path('blogposts/', BlogListView.as_view(), name='blogposts'),
]