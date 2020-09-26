from django.db import models
from django.contrib.auth.models import User


class Reunion(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Sr_No = models.AutoField(primary_key=True)
    Date = models.DateField(blank=True)
    Time = models.TimeField(blank=True)
    Title = models.CharField(max_length=20, null=True, blank=True)
    Memo = models.TextField(null=True, blank=True)
    Place = models.CharField(max_length=50, blank=True, null=True)
    Batch = models.CharField(max_length=7, default='0000-00')
    Participants = models.ManyToManyField(User, default=None, blank=True, related_name='Participants')

    def _str_(self):
        return self.Memo

    @property
    def num_likes(self):
        return self.Participants.all().count()


class List(models.Model):
    LIKE_OPTIONS = (
        ("I'm In", "I'm In"),
        ("I'm Out", "I'm Out"),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    participants = models.CharField(choices=LIKE_OPTIONS, default="I'm In", max_length=10)

    def _str_(self):
        return self.reunion
