from django.db import models
from django.contrib.auth.models import User

GENDER = (
    ('male', 'MALE'),
    ('female', 'FEMALE')
)

# Profile model has one to one relationship with the user model since every user can have only one profile
class Profile(models.Model):
    username    = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    profession  = models.CharField(max_length = 50)
    gender      = models.CharField(max_length = 10, choices = GENDER, default = 'Select')
    profile_img = models.ImageField(blank = True, null = True)

    def __str__(self):
        return '{}'.format(self.username)


# The post model has ForeignKey from Profile models because multiple posts can be posted by a user
class Post(models.Model):
    author          = models.ForeignKey(Profile, on_delete = models.CASCADE)
    title           = models.CharField(max_length = 50)
    about           = models.CharField(max_length = 100)
    article         = models.TextField()
    publish_date    = models.DateTimeField(null = True)
    modified_date   = models.DateTimeField(null = True)

    def __str__(self):
        return '{}'.format(self.title)


class Comment(models.Model):
    reader = models.ForeignKey(Profile, on_delete = models.CASCADE)
    article = models.ManyToManyField(Post)
    comment = models.TextField()
    liked = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)
