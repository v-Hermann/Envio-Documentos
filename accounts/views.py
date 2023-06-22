from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_success')  # redirecionar para a página inicial após o cadastro
    else:
        form = CustomUserCreationForm()
    return render(request, 'account/signup.html', {'form': form})