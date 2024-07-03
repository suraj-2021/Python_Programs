from django.db import models

class BookManager(models.Manager):
      def published_after(self, year=None):
          if year is not None: 
                return self.filter(original_publication_year__gte=year)
          else:
                return self.get_queryset()


class Book(models.Model):
      title = models.CharField(max_length=40)
      original_publication_year = models.IntegerField(blank=True, null=True)
      language_code = models.CharField(max_length=50)
      author = models.ManyToManyField("Author")
      objects = BookManager()

      def __str__(self):
        return self.title
