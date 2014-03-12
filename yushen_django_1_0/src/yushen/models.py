from django.db import models

# Create your models here.

class Part(models.Model):
    def __unicode__(self):
        return self.identifier
    identifier = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    elevator = models.CharField(max_length=200)
    visibility = models.BooleanField(default = True)