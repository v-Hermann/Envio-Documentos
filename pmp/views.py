from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FilesUploaded, DocumentPending
from django.db.models import Q
import re
import string
import unicodedata
from django.contrib import messages


MAX_FILE_SIZE_MB = 5  # Defina o tamanho máximo permitido em ‘megabytes’


@login_required
def fileupload(request):
    if request.method == 'GET':
        return render(request, 'pmp/fileupload.html')
    elif request.method == 'POST':
        file_uploaded = request.FILES.get('filename')
        file = FilesUploaded(titulo=file_uploaded.name, path_doc=file_uploaded)
        file.save()
        return HttpResponse('Enviado!')


DOCUMENT_NAMES = [
    'Registro de Empregado Preenchido',
    'Carteira de Identidade/CPF',
    'Comprovante de Residência',
    'Grau de Instrução',
    'Carteira do Conselho Regional de sua categoria',
    'Título de Eleitor',
    'Certidão do Cartório Eleitoral (que comprova quitação com as obrigações legais)',
    'Certidão de Casamento e de filhos (menores de 14 anos)',
    'CPF dos dependentes (caso tenha)',
    'Certificado de Reservista (masculino)',
    'Declaração de Bens ou Imposto de Renda',
    'Declaração de que não é aposentado por invalidez',
    'Certidão de não acúmulo preenchida',
    'Declaração de Nepotismo',
    'Atestado de Saúde Ocupacional (ASO)',
    'Certidão Negativa Criminal',
    'Certidão Negativa Criminal PF',
    'Declaração negativa de penalidades administrativas'
]


def document_approval_form(request):
    documents_pending = DocumentPending.objects.filter(author=request.user, status='disapproved')
    documents_with_status = DocumentPending.objects.filter(
        Q(author=request.user, status='pending') | Q(author=request.user, status='approved')
    )

    if documents_with_status:
        # Only load documents that need to be resubmitted
        document_names = [doc.title for doc in documents_pending]
        context = {
            'document_names': document_names,
            'success_message': '',
            'error_message': 'Tem documento/s que precisam ser reenviados'
        }

        if request.method == 'POST':
            error_messages = []
            for i, doc in enumerate(documents_pending):
                new_file = request.FILES.get(f'document_{i + 1}')
                if new_file:
                    if new_file.size > (MAX_FILE_SIZE_MB * 1024 * 1024):
                        error_messages.append(f'O arquivo {doc.title} excede o tamanho máximo permitido (5MB)')
                        continue
                    doc_name = filename_makeup(doc.title)
                    file_extension = new_file.name.split('.')[-1]
                    new_file_name = f'{doc_name}.{file_extension}'
                    doc.file.save(new_file_name, new_file)
                    doc.status = 'pending'
                    doc.save()

            if error_messages:
                context['error_message'] = ' '.join(error_messages)
            else:
                context['success_message'] = 'Documentos reenviados para aprovação.'

    else:
        # Load all documents
        document_names = DOCUMENT_NAMES
        context = {
            'document_names': document_names,
            'success_message': '',
            'error_message': ''
        }

        if request.method == 'POST':
            error_messages = []
            for i, title in enumerate(document_names):
                author = request.user
                file = request.FILES.get(f'document_{i + 1}')
                if not file:
                    error_messages.append(f'Por favor, faça o upload de {document_names[i]}')
                    continue
                elif file.size > (MAX_FILE_SIZE_MB * 1024 * 1024):
                    error_messages.append(f'O arquivo {document_names[i]} excede o tamanho máximo permitido (5MB)')
                    continue
                doc_name = filename_makeup(title)
                file_extension = file.name.split('.')[-1]
                new_file_name = f'{doc_name}.{file_extension}'
                document = DocumentPending.objects.create(title=title, author=author, file=None, status='pending')
                document.file.save(new_file_name, file)
                document.save()

            if error_messages:
                context['error_message'] = ' '.join(error_messages)
            else:
                context['success_message'] = 'Documentos enviados para aprovação.'

    return render(request, 'pmp/document_approval_form.html', context)


def filename_makeup(text):
    def normalize_text(text):
        normalized_text = unicodedata.normalize('NFKD', text)
        return ''.join(c for c in normalized_text if not unicodedata.combining(c))

    # Remove the text inside the parentheses
    text = re.sub(r'\(.*\)', '', text).strip()
    # Normalize text by removing accentuation
    text = normalize_text(text)
    # Split text into words
    words = text.split()
    # Capitalize the first letter of each word
    words = [word.capitalize() for word in words]
    # Join the words with underscores
    text = "_".join(words)
    # Remove consecutive underscores
    text = re.sub(r"_{2,}", "_", text)
    # Remove leading and trailing underscores
    text = text.strip("_")
    return text
