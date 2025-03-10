from django import forms
from .models import Image

from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify


class ImageCreateForm(forms.ModelForm):
     
     def clean_url(self):
          url = self.cleaned_data['url']
          valid_extensions = ['jpg','jpeg']
          extension = url.rsplit['.',1][1].lower()
          if extension not in valid_extensions:
               raise forms.ValidationError('The given Url does not mathch valid extesions.')
      
          return url
    
     def save(self,force_insert=False, force_update=False,commit=True):
         image = super(ImageCreateForm,self).save(commit=False)
         image_url = self.cleaned_data['url']
         image_name = f"{slugify(image.title)},{image_url.rsplit('.',1)[1].lower()}"

         #download the imgage from the given url
         response = request.urlopen(image_url)
         image.image.save(image_name,ContentFile(response.read(),save=False))

         if commit:
           image.save()
           return image


     class Meta:
          model = Image
          fields = ["title","image","description"]
          widgets = {
               'url': forms.HiddenInput
          }

