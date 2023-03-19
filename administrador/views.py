from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


@user_passes_test(lambda u: u.is_superuser)
def home(request):
    return render(request, 'administrador/home.html')


def checa_documents(request):
    return render(request, 'administrador/checa_documentos/index.html')
