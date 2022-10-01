from rest_framework.viewsets import ModelViewSet

from post.api.serializers import PostSerializer, CommentSerializer
from post.models import Post, Comment


class PostViewset(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewset(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
