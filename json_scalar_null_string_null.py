from django.db import models

class SampleModel(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_details = models.JSONField()

    def __str__(self):
        return str(self.customer_details)[:1]  # Corrected the typo here


customer1 = SampleModel.objects.create(customer_details={"key": None})  # JSON scalar null
customer2 = SampleModel.objects.create(customer_details={"key": "null"})  # String 'null'

g
null_objects = SampleModel.objects.filter(customer_details__isnull=True)
string_null_objects = SampleModel.objects.filter(customer_details__exact={"key": "null"})
