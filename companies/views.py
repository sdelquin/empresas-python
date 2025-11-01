from django.conf import settings
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import AddCompanyForm
from .models import Company


def index(request):
    if request.method == 'POST':
        if (form := AddCompanyForm(request.POST)).is_valid():
            form.save()
            messages.success(request, 'Empresa añadida correctamente.')
            return redirect('index')
    else:
        form = AddCompanyForm()
    all_companies = Company.objects.all()
    num_companies = Company.objects.count()
    companies = all_companies[: settings.COMPANY_DISPLAY_LIMIT]
    is_slice = len(companies) < num_companies
    return render(
        request,
        'companies/index.html',
        {
            'companies': companies,
            'num_companies': num_companies,
            'is_slice': is_slice,
            'form': form,
        },
    )
