from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.views import APIView
from .models import Blog
from .serializers import BlogSerializer
import google.auth
from django.http import JsonResponse
from google.auth.transport import requests
from google.oauth2 import id_token



def verify_token(request):
    token = request.data.get('access_token', None)

    if not token:
        return JsonResponse({'detail': 'Access token is required.'}, status=400)

    try:
        # Verify the token
        audience = 'YOUR_GOOGLE_CLIENT_ID'  # Replace with your Google OAuth2 client ID
        id_info = id_token.verify_oauth2_token(token, requests.Request(), audience)

        if id_info['aud'] != audience:
            raise ValueError('Invalid audience.')

        return JsonResponse({'detail': 'Token is valid.'}, status=200)
    except ValueError as e:
        return JsonResponse({'detail': str(e)}, status=401)

class BlogListView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get(self, request, *args, **kwargs):

        token = request.data.get('access_token', None)

        if not token:
            return JsonResponse({'detail': 'Access token is required.'}, status=400)

        try:
            # Verify the token
            audience = 'YOUR_GOOGLE_CLIENT_ID'  # Replace with your Google OAuth2 client ID
            id_info = id_token.verify_oauth2_token(token, requests.Request(), audience)

            if id_info['aud'] != audience:
                raise ValueError('Invalid audience.')

            return self.list(request, *args, **kwargs)
        
        except ValueError as e:
            return JsonResponse({'detail': str(e)}, status=401)
        

    def post(self, request, *args, **kwargs):

        token = request.data.get('access_token', None)

        if not token:
            return JsonResponse({'detail': 'Access token is required.'}, status=400)
        try:
            # Verify the token
            audience = '100699103137135615066'  # Replace with your Google OAuth2 client ID
            id_info = id_token.verify_oauth2_token(token, requests.Request(), audience)

            if id_info['aud'] != audience:
                raise ValueError('Invalid audience.')
            
            return self.create(request, *args, **kwargs)
        
        except ValueError as e:
            return JsonResponse({'detail': str(e)}, status=401)
       
