from rest_framework import serializers
from .models import Post, Comment, Rating


class PostSerializer(serializers.ModelSerializer):
    average_rating = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'text', 'publication_date', 'user', 'average_rating']

    def get_average_rating(self, obj):
        return obj.average_rating()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'author', 'text', 'publication_date']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'post', 'user', 'rating']
