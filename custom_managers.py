# myapp/managers.py

from django.db import models

class CustomModelManager(models.Manager):
    def get_active(self):
        """Returns only active records."""
        return self.filter(is_active=True)

    def get_by_name(self, name):
        """Returns a record by name."""
        return self.get(name=name)
