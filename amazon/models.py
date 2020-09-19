from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime,date
# Create your models here.
class Destination(models.Model):

    name = models.CharField(max_length= 30)
    image = models.ImageField(upload_to= 'picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField( default=False )
    marked = models.BooleanField( default=False )
    def __str__(self):
        return self.name
    def show_desc(self):
        return self.desc[:50]

class Testimonial(models.Model):

    test_desc = models.TextField()
    test_writer = models.CharField(max_length=30)
    test_user = models.CharField(max_length=10)

class News(models.Model):
    title = models.CharField(max_length=100)
    body =  RichTextField()
    author = models.CharField(max_length=30)
    purchase_date = models.DateField(auto_now=False,auto_now_add=False,blank=True)
    modified_date = models.DateTimeField(auto_now=False,auto_now_add=True,blank=False)
    image = models.ImageField()
    