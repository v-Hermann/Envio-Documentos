from django.shortcuts import render

def home(request):
    return render(request, 'administrador/home/home.html')


def checa_documents(request):
    return render(request, 'administrador/checa_documentos/index.html')