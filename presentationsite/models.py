from django.db import models

class EmailModel(models.Model):
    email = models.EmailField(unique=True, blank=False)
