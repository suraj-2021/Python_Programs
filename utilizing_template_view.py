#views.py
from django.views.generic import TemplateView

class MyView(TemplateView):
      template = "my_app/about.html"

#url for navigation for navigation to this view
from django.urls import path
from .views import MyView

urlpatterns = [
      path('/about_us', MyView.as_view(), name='about_us')
]
