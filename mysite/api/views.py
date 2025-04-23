from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response, status
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework.views import APIView


# Create your views here.

class BlogPostList(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'  # Use 'id' as the lookup field instead of the default 'pk'

class BlogPostDetail(APIView):

    def get(self, request, pk):
        try:
            blog_post = BlogPost.objects.get(pk=pk)
            serializer = BlogPostSerializer(blog_post)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except BlogPost.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)