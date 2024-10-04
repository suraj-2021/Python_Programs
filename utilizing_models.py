from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class Tag(models.Model):
      title = models.CharField(max_length=200)
      slug = models.CharField(max_length=250, blank=True,null=True)

      def save(self):
            self.slug = slugify(self.title)
            super(Tag,self).save
            
      def __str__(self):
            return self.title


class Flower(models.Model):
      
      title = models.CharField(max_length=100)
      description = models.TextField()
      slug = models.SlugField(blank=True,default='')
      tags = models.ManyToManyField(Tag,blank=True)

      def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super(Flower,self).save     


      def get_absolute_url(self):
            return reverse('detail',args=[str(self.id)])

      def __str__(self):
            return self.title
