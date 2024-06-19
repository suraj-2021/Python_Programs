from django.db import models
from django.db.models import F

class Entry(models.Model):
    name = models.CharField(max_length=150)
    copies_sold = models.IntegerField()
    copies_printed = models.IntegerField()

    def __str__(self):
        return self.name

# Query to find entries where copies sold are greater than or equal to copies printed
business_1 = Entry.objects.filter(copies_sold__gte=F("copies_printed"))

# Query to find entries where copies sold are less than or equal to copies printed
business_2 = Entry.objects.filter(copies_sold__lte=F("copies_printed"))
