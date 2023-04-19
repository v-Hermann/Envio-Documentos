from django.db import models
from django.contrib.auth.models import User


class FilesUploaded(models.Model):
    titulo = models.CharField(max_length=40, null=True)
    path_doc = models.ImageField(upload_to='professor/username/', null=True)

    def __str__(self):
        return self.title


class Document(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents_pending/')
    status = models.CharField(max_length=10, default='pending')
    uploaded_at = models.DateTimeField(auto_now_add=True)
