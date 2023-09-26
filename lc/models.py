from django.db import models
from django.urls import reverse
# Create your models here.
class users(models.Model):
    title=models.CharField(max_length=255,verbose_name='Заголовок')
    content=models.TextField(blank=True)
    photo=models.ImageField(upload_to="uploads/%Y/%m/%d/", verbose_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update= models.DateTimeField(auto_now=True)
    is_published= models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')

    class Meta:
        verbose_name='Известные женщины'
        verbose_name_plural='Известные женщины'
        ordering=['-time_create','title']
    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse('showpost', kwargs={'postid':self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True,verbose_name='Категория')
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'
        ordering=['id']

    def __str__(self):
        return self.name

    def get_absolute_url (self):
        return reverse('showcat', kwargs={'catid':self.pk})