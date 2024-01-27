from django.db import models

class Topics(models.Model):
      name=models.CharField(max_length = 120)
      date_added = models.DateTimeField()
      class Meta:
            verbose_name_plural = 'Toipcs'
      def __str__(self):
          return self.name

class Entry(models.Model):
      topic = models.ForeignKey(Topics,on_delete = models.CASCADE,default='0000000')
      text = models.TextField(max_length = 200,default='0000009')
      date_added = models.DateTimeField(auto_now_add=True)

      class Meta:
            verbose_name_plural = 'entries'
      def __str__(self):
         return f"{self.text[:50]}..."
