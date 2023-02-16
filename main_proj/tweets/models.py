from django.db import models

# Create your models here.

class Tweet(models.Model):
    # id = models.AutoField(primary_key = True)
    # An image for the Tweet, you may add->
    # 'blank=True' it is not required in Django model, 'null=True' means it's not required in the database
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True) 
     
