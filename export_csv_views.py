import csv
from django.http import HttpResponse
from .models import MyModel

def export_to_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="export.csv"'

    writer = csv.writer(response)
    writer.writerow(['field1', 'field2', 'field3'])

    for obj in MyModel.objects.all():
        writer.writerow([obj.field1, obj.field2, obj.field3])

    return response
