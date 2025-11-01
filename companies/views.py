from django.contrib import messages
from django.shortcuts import render

from .forms import AddCompanyForm
from .models import Company


def index(request):
    if request.method == 'POST':
        if (form := AddCompanyForm(request.POST)).is_valid():
            form.save()
            messages.success(request, 'Empresa añadida correctamente.')
            form = AddCompanyForm()
    else:
        form = AddCompanyForm()
    companies = Company.objects.all()
    return render(request, 'companies/index.html', {'companies': companies, 'form': form})
