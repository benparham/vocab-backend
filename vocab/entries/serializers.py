from rest_framework import serializers

from vocab.exceptions import InternalError

from entries.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = (
            'id',
            'word',
            'definition',
            'definition_source'
        )

    def create(self, validated_data):
        request = self.context.get('request', None)
        if not request:
            raise InternalError
        validated_data['owner'] = request.user
        return Entry.objects.create(**validated_data)
