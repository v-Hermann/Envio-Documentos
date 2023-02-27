from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    ''' Homepage temporária '''
    return HttpResponse('Homepage')

def fileupload(request):
    return render(request, 'fileupload.html')