from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import os


class Document(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    file = models.FileField(upload_to='documents/')
    status = models.CharField(max_length=10, default='pending')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save_to_user_folder(self, user):
        user_profile = user.userprofile
        filename = os.path.basename(self.file.name)
        user_folder = user_profile.documents_folder
        user_folder_path = os.path.join(settings.MEDIA_ROOT, user_folder)
        if not os.path.exists(user_folder_path):
            os.makedirs(user_folder_path)
        destination_path = os.path.join(user_folder_path, filename)
        if os.path.exists(destination_path):
            os.remove(destination_path)
        os.rename(self.file.path, destination_path)
        self.file.name = os.path.join(user_folder, filename)
        self.save()
