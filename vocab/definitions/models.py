from django.db import models

from entries.models import Entry

class Definition(models.Model):
    entry = models.ForeignKey(Entry, related_name='definitions')
    text = models.TextField()
    rank = models.IntegerField()
    source = models.CharField(max_length=256, null=True)
