from django import forms
from django.utils.safestring import mark_safe

from .models import Company


class AddCompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        exclude = ['slug']
        widgets = {
            'remarks': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
        for field_name, field in self.fields.items():
            if field.required:
                field.label = mark_safe(
                    f'{field.label}<sup><i class="fa-solid fa-asterisk pico-color-pink"></i></sup>'
                )

    def clean_name(self):
        name = self.cleaned_data['name']
        if self._meta.model.objects.filter(name__iexact=name).exists():
            raise forms.ValidationError('Ya existe una empresa con este nombre.')
        return name
