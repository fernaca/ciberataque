from distutils.command import upload
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Banco(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return (self.name ) 

# Adonde mandar despues de la creacion
    def get_absolute_url(self):
        return reverse('home')

class Post(models.Model):
    title = models.CharField(max_length=255)
    header_image = models.ImageField(null=True,blank=True, upload_to="images/")
#    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #body = models.TextField()
    body = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    # Fecha y hora
    created_on = models.DateTimeField(auto_now_add=True)
    # Solo fecha
    created_on = models.DateField(auto_now_add=True)
    banco = models.ForeignKey(Banco, on_delete=models.CASCADE, default=None,related_name="banco")
 
# Default human-readable representation of the object.
# Django will use it in many places, such as the administration site.
    def __str__(self):
        return 'Creado el: ' + str(self.created_on) + ' - ' + self.title 

    class Meta:
        ordering = ['-created_on']

# Adonde mandar despues de la creacion
    def get_absolute_url(self):
        #        return reverse('detail', args=(str(self.id)))
        return reverse('home')
