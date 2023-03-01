from django.shortcuts import render
from django.http import HttpResponse
from .models import FilesUploaded

def home(request):
    ''' Homepage temporária '''
    return HttpResponse('Homepage')

def fileupload(request):
    if request.method == 'GET':
        return render(request, 'pmp/fileupload.html')
    elif request.method == 'POST':
        file_uploaded = request.FILES.get('filename')
        file = FilesUploaded(titulo=file_uploaded.name, path_doc=file_uploaded)
        file.save()
        return HttpResponse('Enviado!')
