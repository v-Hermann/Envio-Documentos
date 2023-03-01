# Generated by Django 4.1.5 on 2023-03-01 01:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pmp', '0002_rename_fileupload_filesuploaded'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='filesuploaded',
            name='document_generic',
        ),
        migrations.AddField(
            model_name='filesuploaded',
            name='path_doc',
            field=models.ImageField(null=True, upload_to='professor/username/'),
        ),
        migrations.AddField(
            model_name='filesuploaded',
            name='titulo',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
