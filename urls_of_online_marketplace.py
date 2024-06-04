from django.urls import path
from django.conf import settings 
from django.conf.urls.static import static
from.import views

app_name = 'item'

urlpatterns = [
    path('newitem/',views.new,name='newitem'),
    path('item/<int:pk>/',views.detail, name='detail'),
    path('<int:pk>/delete', views.delete, name='delete'),
    path('<int:pk>/edit/', views.edit, name ='edit'),
    path('',views.items, name = 'items'),

   
]

