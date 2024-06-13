from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    copies_sold = models.IntegerField()

    @property
    def is_bestseller(self):
        return self.copies_sold > 50000
