from django.db import models

# Create your models here.
class DocPlace(models.Model):
    Filename = models.CharField(max_length=128)
    File = models.TextField(max_length=3000)
    def __str__(self):
        return self.Filename

