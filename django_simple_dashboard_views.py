from django.shortcuts import render
from .models import DataModel

def dashboard(request):
    data = DataModel.objects.all()
    return render(request, 'dashboard.html', {'data': data})
