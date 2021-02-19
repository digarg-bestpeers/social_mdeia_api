from network.models import Post, User
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from network.api.serializers import PostSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

from django.shortcuts import render, get_object_or_404



class PostList(ListAPIView):
  serializer_class = PostSerializer

  def get_queryset(self):
    queryset = Post.objects.filter(user=self.request.user)
    return queryset


class PostCreate(CreateAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all().order_by('-id')[:1]

class PostDestroy(DestroyAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class PostUpdate(UpdateAPIView):
  serializer_class = PostSerializer
  queryset = Post.objects.all()


class AllPostList(ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializer


class SearchPost(APIView):
  def get(self, request, format=None):
    search_data = request.GET.get('srch')
    posts = Post.objects.filter(body__contains=search_data)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)


class LikePost(APIView):
  def get(self, request, format=None):
    post = get_object_or_404(Post, id=request.GET.get('id'))
    import pdb; pdb.set_trace()
