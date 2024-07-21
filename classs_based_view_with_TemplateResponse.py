from django.views import View
from django.template.response import TemplateResponse

class FoundMyFitnessClass(View):
    template_name = "my_app/my_name.html"

    def get(self, request):
        context = {"message": "Hello World! this is the message"}
        return TemplateResponse(request, self.template_name, context)
