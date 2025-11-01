from django import template
from django.utils.safestring import mark_safe

from companies.models import Company

register = template.Library()


@register.filter
def title(company: Company) -> str:
    if company.website:
        return mark_safe(f'<a href="{company.website}">{company.name}</a>')
    return company.name


@register.filter
def is_remote(company: Company) -> str:
    if company.remote:
        return mark_safe('<i class="fa-solid fa-check"></i>')
    return mark_safe('<i class="fa-solid fa-xmark"></i>')
