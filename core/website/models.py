from django.db import models

# Create your models here.

class Newsletter(models.Model):
    email=models.EmailField(max_length=255)
    

    def __str__(self):
        return self.email
