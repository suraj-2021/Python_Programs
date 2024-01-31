# views.py
from django.views.generic import TemplateView
from .models import MyModel # replace with your model name

class MyView(TemplateView): # replace with your view name
    template_name = "my_template.html" # replace with your template name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["my_model"] = MyModel.objects.all() # replace with your model query
        return context
