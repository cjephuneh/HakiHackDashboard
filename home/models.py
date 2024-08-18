from django.db import models

# Create your models here.

class Govpersonnel(models.Model):
    
    image = models.ImageField(upload_to="civic_personel")
    name  = models.CharField(max_length = 100, blank=True) 
    email  = models.EmailField(max_length = 100, blank=True)
    service_number = models.CharField(blank=True, max_length = 100)
    
    def __str__(self):
        return self.image.url
   