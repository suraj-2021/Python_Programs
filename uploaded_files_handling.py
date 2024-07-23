from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ModelWithFile

def uploading_file(request):
    if request.method == "POST":
        form = ModelWithFile(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')  # Redirect to a success page
    else:
        form = ModelWithFile()

    return render(request, 'my_app/mytemplate.html', {"form": form})
