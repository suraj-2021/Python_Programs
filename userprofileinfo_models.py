from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfileInfo(models.Model):
      user = models.OneToOneField(User)
      
      #add additional attrubutes as you need
      portfolio = models.URLField(User)
      picture = models.ImageField(upload_to = 'profile_pics')

      def __str__(self):
            return self.user.username
