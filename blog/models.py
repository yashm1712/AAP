from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Sr_No = models.AutoField(primary_key=True)
    time = models.DateTimeField(auto_now_add=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    pic = models.ImageField(upload_to="blog", default="", blank=True, null=True)
    liked = models.ManyToManyField(User, default=None, blank=True, related_name='liked')

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all().count()


class Comment(models.Model):
    S_No = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_c = models.ForeignKey(Blog, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.comments[0:10]


class Like(models.Model):

    LIKE_OPTIONS = (
        ('Like', 'Like'),
        ('Unlike', 'Unlike'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    likes = models.CharField(choices=LIKE_OPTIONS, default='Like', max_length=10)

    def _str_(self):
        return self.user.first_name + self.user.last_name