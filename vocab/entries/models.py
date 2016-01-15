from django.db import models
from django.conf import settings

from entries.tasks import wordnik_define

class EntryManager(models.Manager):
    def create(self, **validated_data):
        entry = Entry(**validated_data)
        entry.save()

        # wordnik_define.delay(entry.id)
        wordnik_define(entry.id)
        return entry


class Entry(models.Model):
    class Meta:
        ordering = ['-created_date']

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='entries')
    word = models.CharField(max_length=256)
    created_date = models.DateTimeField(auto_now_add=True)

    objects = EntryManager()
