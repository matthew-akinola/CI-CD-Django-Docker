from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer



class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
