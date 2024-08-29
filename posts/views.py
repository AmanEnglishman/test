from rest_framework import generics
from .models import Post, Comment, Rating
from .permissions import IsPostAuthorOrIsStaff
from .serializers import PostSerializer, CommentSerializer, RatingSerializer
from telegram import Bot

from .service import send_telegram_message


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = IsPostAuthorOrIsStaff


class PostCreateAPIView(generics.CreateAPIView):
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        post = serializer.save()
        send_telegram_message(post.user.telegram_chat_id, f"Ваш {post.id} был опубликован")


class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        serializer.save(post_id=post_id)


class RatingCreateAPIView(generics.CreateAPIView):
    serializer_class = RatingSerializer
    queryset = Rating.objects.all()
