from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from accounts.forms import CustomUserChangeForm
from accounts.models import CustomUser


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

