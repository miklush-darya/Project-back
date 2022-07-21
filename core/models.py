from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created = models.DateTimeField("Created", auto_now_add=True, blank=True, null=True)
    modified = models.DateTimeField("Created", auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True