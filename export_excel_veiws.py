from django.http import HttpResponse
from .models import MyModel
import pandas as pd

def export_excel(request):
    # Query the database for all objects
    data = MyModel.objects.values('field1', 'field2', 'field3')

    # Convert the data to a pandas DataFrame
    df = pd.DataFrame.from_records(data)

    # Create a HttpResponse object with the appropriate CSV header
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="export.xlsx"'

    # Write the DataFrame to the HttpResponse object
    df.to_excel(response, index=False, engine='openpyxl')

    return response
