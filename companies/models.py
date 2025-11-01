from django.db import models
from django.utils.text import slugify


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Nombre de la empresa')
    slug = models.SlugField(unique=True)
    email = models.EmailField(verbose_name='Correo electrónico')
    city = models.CharField(max_length=255, blank=True, verbose_name='Ciudad')
    contact_person = models.CharField(
        max_length=255, blank=True, verbose_name='Persona de contacto'
    )
    phone = models.CharField(max_length=20, blank=True, verbose_name='Teléfono o móvil de empresa')
    website = models.URLField(blank=True, null=True, verbose_name='Página web')
    remote = models.BooleanField(default=False, verbose_name='Remoto')
    remarks = models.TextField(blank=True, verbose_name='Observaciones')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'
