from django import forms

from .models import Company


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'email', 'city', 'contact_person', 'website', 'remote', 'remarks']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }

    def clean_name(self):
        name = self.cleaned_data['name']
        if self._meta.model.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError('Ya existe una empresa con este nombre.')
        return name
