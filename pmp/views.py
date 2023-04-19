from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FilesUploaded, Document
from django.contrib import messages


@login_required
def fileupload(request):
    if request.method == 'GET':
        return render(request, 'pmp/fileupload.html')
    elif request.method == 'POST':
        file_uploaded = request.FILES.get('filename')
        file = FilesUploaded(titulo=file_uploaded.name, path_doc=file_uploaded)
        file.save()
        return HttpResponse('Enviado!')


def document_approval_form(request):
    document_names = [
        'Registro de Empregado Preenchido',
        'Carteira de Identidade/CPF',
        'Comprovante de Residência',
        'Grau de Instrução',
        'Carteira do Conselho Regional de sua categoria',
        'Título de Eleitor',
        'Certidão do Cartório Eleitoral que comprova quitação com as obrigações legais',
        'Certidão de Casamento e de filhos (menores de 14 anos)',
        'CPF dos dependentes (caso tenha)',
        'Certificado de Reservista (masculino)',
        'Declaração de Bens ou Imposto de Renda',
        'Declaração de que não é aposentado por invalidez',
        'Certidão de não acúmulo preenchida',
        'Declaração de Nepotismo',
        'Atestado de Saúde Ocupacional(ASO)',
        'Certidão Negativa Criminal',
        'Certidão Negativa Criminal PF',
        'Declaração de não ter sofrido penalidades administrativas'
    ]
    context = {
        'document_names': document_names
    }
    if request.method == 'POST':
        for i in range(1, 19):
            title = document_names[i - 1]
            author = request.user.profile
            file = request.FILES.get(f'document_{i}')
            if file:
                Document.objects.create(title=title, author=author, file=file, status='pending')
        messages.success(request, 'Documents submitted for approval.')
        return redirect('document_approval')
    return render(request, 'document_approval.html', {'document_names': document_names})
