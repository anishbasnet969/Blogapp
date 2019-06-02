from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    title = models.CharField(max_length = 120)
    slug = models.SlugField(unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title

