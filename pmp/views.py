from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FilesUploaded, DocumentPending
from django.db.models import Q
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
    documents_pending = DocumentPending.objects.filter(author=request.user, status='disapproved')
    documents_with_status = DocumentPending.objects.filter(
        Q(author=request.user, status='pending') | Q(author=request.user, status='approved')
    )

    # If there are no documents to resubmit, load all documents
    if not documents_with_status:
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
            'document_names': document_names,
            'success_message': '',
            'error_message': ''
        }

        if request.method == 'POST':
            for i in range(1, 19):
                title = document_names[i - 1]
                author = request.user
                file = request.FILES.get(f'document_{i}')
                if not file:
                    context['error_message'] = f'Please upload {document_names[i - 1]}'
                    break
                DocumentPending.objects.create(title=title, author=author, file=file, status='pending')
            else:
                context['success_message'] = 'Documentos enviados para aprovação.'
                return render(request, 'pmp/document_approval_form.html', context)

        return render(request, 'pmp/document_approval_form.html', context)

    # Otherwise, load only documents that need to be resubmitted
    else:
        document_names = [doc.title for doc in documents_pending]
        context = {
            'document_names': document_names,
            'success_message': '',
            'error_message': 'Tem documento/s que precisam ser reenviados'
        }

        if request.method == 'POST':
            for i, doc in enumerate(documents_pending):
                # Update the pending document with the new file and status "pending"
                new_file = request.FILES.get(f'document_{i + 1}')
                if new_file:
                    doc.file = new_file
                    doc.status = 'pending'
                    doc.save()
            context['success_message'] = 'Documentos reenviados para aprovação.'
            return render(request, 'pmp/document_approval_form.html', context)

        return render(request, 'pmp/document_approval_form.html', context)

