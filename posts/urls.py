from django.urls import path

from .views import *

urlpatterns = [
    path('post/', PostListAPIView.as_view(), name='posts'),
    path('post_add', PostCreateAPIView.as_view(), name='post_add'),
    path('post/<int:pk>', PostDetailAPIView.as_view(), name='post_detail'),
    path('post/update/<int:pk>', PostUpdateDeleteAPIView.as_view(), name='post_update_delete'),
    path('post/<int:post_id>/comment', CommentListAPIView.as_view(), name='comment'),
    path('post/<int:post_id>/comment_add', CommentCreateAPIView.as_view(), name='comment_add'),
    path('post/<int:post_id>/rating_add', RatingCreateAPIView.as_view(), name='rating_add'),


]