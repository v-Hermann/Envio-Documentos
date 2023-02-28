from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from .models import FilesUploaded

def home(request):
    ''' Homepage temporária '''
    return HttpResponse('Homepage')

def fileupload(request):
    file = get_object_or_404(FilesUploaded, pk=1)

    if request.method == 'POST':
        form = forms.FileUpload(request.POST)
        if form.is_valid():
            file.document_generic = form.generic_file
            file.save()
            return HttpResponse('Enviado!')
    else:
        form = FilesUploaded()
        context = {
            'form': form,
        }

        return render(request, 'pmp/fileupload.html', context=context)
