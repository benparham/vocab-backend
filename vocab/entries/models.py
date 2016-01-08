from django.db import models
from django.conf import settings

from entries.tasks import wordnik_define

class EntryManager(models.Manager):
    def create(self, **validated_data):
        entry = Entry(**validated_data)
        entry.save()

        wordnik_define.delay(entry.id)

        return entry

class Entry(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='entries')
    word = models.CharField(max_length=256)
    definition = models.TextField(null=True)
    definition_source = models.CharField(max_length=256, null=True)

    objects = EntryManager()
