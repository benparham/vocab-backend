from __future__ import absolute_import

from celery import shared_task

from django.conf import settings

import requests

WORDNIK_URL = 'https://api.wordnik.com/v4/word.json/'
MAX_DEFINITIONS = 3


# TODO: useCanonical will turn things like cats -> cat (part of wordnik API)
@shared_task
def wordnik_define(entry_id):
    if (settings.WORDNIK_API_KEY == None):
        raise Exception('Wordnik api key not set')
        return

    # Import within method to avoid circular/recursive import
    from entries.models import Entry
    from definitions.models import Definition
    entry = Entry.objects.get(id=entry_id)

    r = requests.get(
            WORDNIK_URL + entry.word + '/definitions/',
            params={'api_key': settings.WORDNIK_API_KEY}
        )

    if (r.status_code == 200):
        results = r.json()
        for i in range(0, min(MAX_DEFINITIONS, len(results))):
            result = results[i]

            definition = Definition(entry=entry)
            definition.text = result['text']
            definition.part_of_speech = result['partOfSpeech']
            definition.source = result['sourceDictionary']
            definition.rank = i + 1

            definition.save()
