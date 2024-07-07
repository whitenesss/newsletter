from django.db import models


# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    content = models.TextField(verbose_name='содержание')
    image = models.ImageField(upload_to="blog", verbose_name='изображение', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='время создания')
    count_view = models.IntegerField(default=0, verbose_name='количество просмотров')
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title
