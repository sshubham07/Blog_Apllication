from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.utils.text import slugify
CATEGORY=[('politics','politics'),
('Sports','Sports'),
('Busines', 'Busines'),
('Education','Education'),
('Other', 'Other'),
('Entertainment','Entertainment')]

# Create your models here.
class MyBlog(models.Model):
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    title= models.CharField(max_length = 200)
    body = RichTextField(blank=True, null=True)
    image= models.ImageField(upload_to ='images')
    datetime = models.DateTimeField(auto_now= True)
    category=models.CharField(max_length=15,choices=CATEGORY,default='Other')
    slug = models.SlugField(max_length=40,null=False,unique=True)
    def __str__(self):
        return self.title

    
