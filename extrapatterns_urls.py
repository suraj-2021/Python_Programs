from django.urls import path, include
from app import views as app_views
from program import views as program_views

extrapatterns = [
    path("name/", program_views.name),
    path("address/", program_views.address),
    path("courses/", program_views.courses),
]

urlpatterns = [
    path("", app_views.home),
    path("program/", include(extrapatterns)),
]
