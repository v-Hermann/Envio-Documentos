from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import redirect, render


def login_success(request):
    if request.user.is_superuser:
        return redirect("home")
    else:
        return redirect("fileupload")


@login_required
@user_passes_test(lambda u: u.is_superuser)
def home(request):
    
    user = 0
    context = {
        'user': user,
    }

    return render(request, 'administrador/home.html', context=context)


@login_required
@user_passes_test(lambda u: u.is_superuser)
def checa_documents(request):
    return render(request, 'administrador/checa_documentos.html')
