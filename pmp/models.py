from django.db import models


class FilesUploaded(models.Model):
    titulo = models.CharField(max_length=40, null=True)
    path_doc = models.ImageField(upload_to='professor/username/', null=True)

    def __str__(self):
        return self.title
