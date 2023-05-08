from django.db import models
from django.contrib.auth import get_user_model


class FilesUploaded(models.Model):
    titulo = models.CharField(max_length=40, null=True)
    path_doc = models.ImageField(upload_to='professor/username/', null=True)

    def __str__(self):
        return self.title


def upload_to(instance, filename):
    return f"documents_pending/{instance.author.pk}_{instance.author.fullname}/{filename}"


class DocumentPending(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    file = models.FileField(upload_to=upload_to)
    status = models.CharField(max_length=10)
    uploaded_at = models.DateTimeField(auto_now_add=True)
