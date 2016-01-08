from __future__ import absolute_import

from celery import shared_task

from django.conf import settings

import requests

WORDNIK_URL = 'https://api.wordnik.com/v4/word.json/'

@shared_task
def wordnik_define(entry_id):
    if (settings.WORDNIK_API_KEY == None):
        print('Wordnik api key not set')
        return

    # Import within method to avoid circular/recursive import
    from entries.models import Entry
    entry = Entry.objects.get(id=entry_id)

    r = requests.get(
            WORDNIK_URL + entry.word + '/definitions/',
            params={'api_key': settings.WORDNIK_API_KEY}
        )

    if (r.status_code != 200):
        entry.definition = 'Definition not found'
    else:
        result = r.json()[0]
        entry.definition = result['text']
        entry.definition_source = result['sourceDictionary']
    entry.save()
