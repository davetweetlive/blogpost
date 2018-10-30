from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('male', 'MALE'),
    ('female', 'FEMALE')
)

class Profile(models.Model):
    username    = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    profession  = models.CharField(max_length = 50)
    gender      = models.CharField(max_length = 10, choices = GENDER, default = 'Select')

    def __str__(self):
        return '{}'.format(self.username)

class Post(models.Model):
    author          = models.ForeignKey(Profile, on_delete = models.CASCADE)
    title           = models.CharField(max_length = 50)
    article         = models.TextField()
    publish_date    = models.DateTimeField(null = True)
    modified_date   = models.DateTimeField(null = True)

    def __str__(self):
        return '{}'.format(self.title)
