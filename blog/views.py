from django.shortcuts import render
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics, mixins
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request, *args, **kwargs):
        order = self.request.query_params.get('order')

        if order == 'user':
            queryset = self.filter_queryset(self.get_queryset().order_by('user__email'))
        elif order == 'updated':
            queryset = self.filter_queryset(self.get_queryset().order_by('-updated_at'))
        else:
            queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# GenericAPIView 파생 views1
# class PostCreateAPIView(generics.CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostListAPIView(generics.ListAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostRetrieveAPIView(generics.RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostUpdateAPIView(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDestroyAPIView(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer



# GenericAPIView 파생 views2
# class PostListCreateAPIView(generics.ListCreateAPIView):
    
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

