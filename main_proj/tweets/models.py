from django.db import models
import random
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL



class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey("Tweet", on_delete=models.CASCADE)

class Tweet(models.Model): #default=1---> is actually the default user which is the superuser(malik)
    user = models.ForeignKey(User, on_delete= models.CASCADE) # Many users can have many tweets....
    id = models.AutoField(primary_key = True)
    likes = models.ManyToManyField(User, related_name='tweet_user', blank=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True) 

    class Meta: ## This class will order our tweets. As the newest tweets/// Notice the minus sign 
        ordering = ['-id']
     
    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(1, 200)
        }