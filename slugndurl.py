from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Flower(models.Model):
      
      title = models.CharField(max_length=100)
      description = models.TextField()
      slug = models.SlugField(blank=True, default='')

      def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super(Flower,self).save     


      def get_absolute_url(self):
            return reverse('detail',args=[str(self.id)])

      def __str__(self):
            return self.title
