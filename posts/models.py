from django.db import models
from users.models import CustomUser


class Post(models.Model):
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def average_rating(self):
        ratings = self.ratings.all()
        if ratings:
            return sum(r.rating for r in ratings) / len(ratings)
        return 0


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=150)
    text = models.TextField()
    publication_date = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    post = models.ForeignKey(Post, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
