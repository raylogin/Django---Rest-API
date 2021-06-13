from django.db import models

class router(models.Model):
    sapid = models.CharField(max_length=18)
    hostname = models.CharField(max_length=14)
    loopback = models.CharField(max_length=15)
    type = models.CharField(max_length=4)
    def __str__(self):
        return self.hostname