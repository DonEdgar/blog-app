from django.db import models
from django.urls import reverse

class Post(models.Model):
    """
    This model class is the table for a single blog posts
    """
    title = models.CharField(max_length=200) 
    # Using a foreign key which allows for for a many-to-one relationship
    # allows for a user to be the author of many different blog posts
    # The reference key is built in User model for Django with authentication
    author = models.ForeignKey(
            'auth.User', 
            on_delete=models.CASCADE,
            )
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
