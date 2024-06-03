from django.db import models

# Create your models here.


class Usuario(models.Model):


    id_usuario = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=255, null=False, blank=False)
    lastname = models.CharField(max_length=255, null=False, blank=False)
    email = models.EmailField(max_length=255, null=False, blank=False)
    number = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=255, null=False, blank=False)
    
    
    def __str__(self):
        return self.first_name