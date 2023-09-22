from django.db import models
from django.urls import reverse
# Create your models here.
class users(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField(blank=True)
    photo=models.ImageField(upload_to="uploads/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update= models.DateTimeField(auto_now=True)
    is_published= models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    def __str__ (self):
        return self.title

    def get_absolute_url (self):
        return reverse('showpost', kwargs={'postid':self.pk})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url (self):
        return reverse('showcat', kwargs={'catid':self.pk})