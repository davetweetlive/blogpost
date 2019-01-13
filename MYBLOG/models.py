from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


GENDER = (
    ('male', 'MALE'),
    ('female', 'FEMALE')
)

# Profile model has one to one relationship with the user model since every user can have only one profile
class Profile(models.Model):
    username    = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    profession  = models.CharField(max_length = 50)
    gender      = models.CharField(max_length = 10, choices = GENDER, default = 'Select')
    profile_img = models.ImageField(default = 'default.png', upload_to = 'profile_pics', blank = True, null = True)
    website     = models.CharField(max_length = 50, null=True)
    mobile      = models.IntegerField(null = True)
    location    = models.CharField(max_length = 30, null = True,)

    def __str__(self):
        return '{}'.format(self.username)


# The following function user_is_created creates an user's profile with default data when a user does registration
@receiver(post_save, sender=User)
def user_is_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(username=instance)
    else:
        instance.profile.save()


# The post model has ForeignKey from Profile models because multiple posts can be posted by a user
class Post(models.Model):
    author          = models.ForeignKey(Profile, on_delete = models.CASCADE)
    title           = models.CharField(max_length = 50)
    about           = models.CharField(max_length = 100)
    article         = models.TextField()
    publish_date    = models.DateTimeField(null = True)
    modified_date   = models.DateTimeField(null = True)
    # article_img     = models.ImageField(default = 'default.gpg', upload_to = '_pics', blank = True, null = True)

    def __str__(self):
        return '{}'.format(self.title)


class Comment(models.Model):
    reader = models.ForeignKey(Profile, on_delete = models.CASCADE)
    article = models.ManyToManyField(Post)
    comment = models.TextField()
    liked = models.BooleanField(default=False)
    disliked = models.BooleanField(default=False)
