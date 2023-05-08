from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from accounts.forms import CustomUserChangeForm
from accounts.models import CustomUser
from pmp.models import DocumentPending
from django.http import FileResponse, Http404
from django.views.decorators.clickjacking import xframe_options_exempt
import os


def login_success(request):
    if request.user.is_superuser:
        return redirect("home")
    else:
        return redirect("fileupload")


@login_required
@user_passes_test(lambda u: u.is_superuser)
def home(request):
    return render(request, 'administrador/home.html')


@login_required
@user_passes_test(lambda u: u.is_superuser)
def checa_documents(request):
    return render(request, 'administrador/checa_documentos.html')


@login_required
@staff_member_required
def user_list(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request, 'administrador/alteracao_cadastral.html', {'users': users})


@staff_member_required
@login_required
def edit_user(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User account updated.')
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'administrador/edit_user.html', {'form': form, 'user': user})


def document_approval(request):
    documents = DocumentPending.objects.filter(status='pending')
    if request.method == 'POST':
        action = request.POST.get('action')
        document_id = request.POST.get('document_id')
        document = get_object_or_404(DocumentPending, id=document_id)
        if action == 'approve':
            # save the document to the user's folder
            document.save_to_user_folder(request.user)
            # delete the document file from the file system
            if os.path.isfile(document.file.path):
                os.remove(document.file.path)
            # delete the document from the approval queue
            document.delete()
            # delete the parent folder if it's empty
            parent_folder = os.path.dirname(document.file.path)
            if not os.listdir(parent_folder):
                os.rmdir(parent_folder)
            messages.success(request, f'Document "{document.title}" has been approved and saved to your folder.')
        elif action == 'disapprove':
            document.status = 'disapproved'
            document.save()
            # delete the parent folder if it's empty
            parent_folder = os.path.dirname(document.file.path)
            if not os.listdir(parent_folder):
                os.rmdir(parent_folder)
            messages.warning(request, f'Document "{document.title}" has been disapproved and removed from the queue.')
        else:
            messages.error(request, 'Invalid action.')
        return redirect('document_approval')
    else:
        return render(request, 'administrador/document_approval.html', {'documents': documents})


@xframe_options_exempt
def document_preview(request, document_id):
    document = get_object_or_404(DocumentPending, id=document_id)
    if document.file:
        # Check if the file is an image or pdf
        if document.file.name.endswith('.pdf'):
            response = FileResponse(document.file, content_type='application/pdf')
            response['X-Frame-Options'] = 'ALLOW-FROM *'
            return response
        elif document.file.name.endswith('.jpg') or document.file.name.endswith('.jpeg') or document.file.name.endswith('.png'):
            return FileResponse(document.file, content_type='image/jpeg')
        else:
            raise Http404("File type not supported.")
    else:
        raise Http404("File not found.")
