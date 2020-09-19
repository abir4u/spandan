from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime , date
from django.contrib.auth.models import User, auth

# Create your models here.
class posts(models.Model):

    post_name = models.CharField(max_length= 150)
    post_image = models.ImageField(upload_to= 'picture')
    #post_desc = models.TextField()
    post_desc = RichTextField(blank='True', null='True')

    post_marked = models.BooleanField( default=True )
    post_catagory = models.CharField(max_length= 15)
    post_publish = models.DateField(default = date.today)
    
    class Meta:
        ordering = ["post_publish"]

class feedback(models.Model):
    fed_name = models.CharField(max_length= 150)
    email =models.CharField(max_length= 100)
    subject=models.CharField(max_length= 200)
    note =models.TextField()

class Comment(models.Model):
    message = models.TextField('Message')
    date = models.DateField(default = date.today)
    user_id = models.ForeignKey(User,on_delete = models.CASCADE)
    post_id = models.ForeignKey(posts,on_delete = models.CASCADE)
    parent = models.ForeignKey('self', null=True,blank=True,related_name = "replies",on_delete = models.CASCADE)
    active = models.BooleanField(default = True )
   
    
    def __str__(self):
        if Comment.parent == True:
            return " reply =    {}    -----  {}".format(self.post_id.post_name,self.user_id.username)
        else:
            return " post =    {}    -----  {}".format(self.post_id.post_name,self.user_id.username)

    class Meta:
        ordering = ('post_id','date',)  