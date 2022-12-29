from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Blog post model for database.
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    image = models.ImageField(null=True, blank=True)

    class Meta:
        """ Display most recent post first. """
        ordering = ['-date']

    def __str__(self):
        """ Display post instance by its title. """
        return str(self.title)

    def snippet(self):
        """ Display snippet of post instance. """
        return self.body[:50] + '...'
