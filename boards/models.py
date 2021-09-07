from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator

# Create your models here.

# adding a new line in master branch

class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = "board"

    def __str__(self):
        return self.name

    def get_posts_count(self):
        return Post.objects.filter(topic__board=self).count()

    def get_last_post(self):
        return Post.objects.filter(topic__board=self).order_by('-created_at').first()




class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics',on_delete = models.CASCADE)
    starter = models.ForeignKey(User, related_name='topics',on_delete = models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    
    class Meta:
        db_table = "topic"

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts',on_delete = models.CASCADE)
    updated_by = models.ForeignKey(User, null=True, related_name='+',on_delete = models.CASCADE)
   
    class Meta:
        db_table = "post"

    def __str__(self):
        truncated_message = Truncator(self.message)
        return truncated_message.chars(30)







class Test:
    name = models.CharField(max_length=100)


# import the standard Django Model
# from built-in library
from django.db import models
  
# declare a new model with a name "GeeksModel"
class MasterModel(models.Model):
        # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = "images/")
  
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.description