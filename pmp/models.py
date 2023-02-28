from django.db import models

class FilesUploaded(models.Model):
    document_generic = models.ImageField(upload_to='professor/username/')