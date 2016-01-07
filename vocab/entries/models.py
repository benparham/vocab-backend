from django.db import models
from django.conf import settings

class Entry(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='entries')
    word = models.CharField(max_length=256)
    definition = models.TextField(null=True)
    definition_source = models.CharField(max_length=256, null=True)
    
