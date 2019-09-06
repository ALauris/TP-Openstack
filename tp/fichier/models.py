from django.db import models

# Create your models here.


class Fichier(models.Model):
    description = models.CharField(max_length=255, blank=True)
    fichier = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)