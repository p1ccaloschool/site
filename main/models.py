from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class Topic(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(unique=True, help_text="ЧПУ для ссылки (например: python-basics)")
    description = models.TextField(blank=True, verbose_name="Краткое описание")
    
    # Визуальный редактор с картинками
    content = CKEditor5Field('Контент', config_name='default')
    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title