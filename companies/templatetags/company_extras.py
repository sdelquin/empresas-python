from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from companies.models import Company

register = template.Library()


@register.filter
def title(company: Company) -> str:
    if company.website:
        return format_html('<a href="{}">{}</a>', company.website, company.name)
    return company.name


@register.filter
def is_remote(company: Company) -> str:
    if company.remote:
        return mark_safe('<i class="fa-solid fa-check"></i>')
    return mark_safe('<i class="fa-solid fa-xmark"></i>')
