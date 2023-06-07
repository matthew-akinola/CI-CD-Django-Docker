from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from blogapp.models import Blog
from blogapp.serializers import BlogSerializer

class MyModelListViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('blogposts')
        self.data = {
            'title': 'How to containerized a django application',
            'body': 'This is a test'
            }

    def test_create_mymodel(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        mymodel = Blog.objects.get(pk=response.data['id'])
        serializer = BlogSerializer(mymodel)
        self.assertEqual(response.data, serializer.data)
