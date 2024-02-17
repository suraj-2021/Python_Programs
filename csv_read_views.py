# views.py

from django.shortcuts import render, redirect
from .forms import CSVImportForm
from .models import Book
import csv

def import_csv(request):
    if request.method == 'POST':
        form = CSVImportForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file'].read().decode('utf-8').splitlines()
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                Book.objects.create(
                    title=row['title'],
                    author=row['author'],
                    publication_year=row['publication_year'],
                    isbn=row['isbn']
                )

            return redirect('success_page')  # Redirect to a success page
    else:
        form = CSVImportForm()

    return render(request, 'import.html', {'form': form})
