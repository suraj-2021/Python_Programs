#Here we will try to implement what createview is doing from start to finish
#Step 1: Defining a Model
#models.py
from django.db import models

class Book(models.Model):
      title = models.CharField(max_length=100)
      author = models.CharField(max_length=100)
      published_date = models.DateField()


#Step:2 Creating a 'CreateView' view in views.py
#Views.py
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Book

class BookCreateView(CreateView):
      model = Book
      fields = ['title','author','published_date']
      template_name = 'book_form.html'
      success_url = reverse_lazy('book-list')

#Step 3: Define the Template
#book_form.html
<form method = "post">
   {%csrf_token%}
   {{form.as_p}}
   <button type = "submit"> Add Book </button>
</form>

#Step 4: Configuring the URLS
#urls.py
from django.urls import path
from .views import  BookCreateView

urlpatterns = [
  path('books/add', BookCreateView.as_view(), name = 'book-add')
]
      
