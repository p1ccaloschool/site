from django.db import models


class Topic(models.Model):
    title = models.CharField(max_length=200)  # Название темы (например, "Python")
    slug = models.SlugField(unique=True)  # ЧПУ для URL (например, "python")
    description = models.TextField()  # Описание
    content = models.TextField()  # Основной контент (Markdown или HTML)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
