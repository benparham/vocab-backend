from rest_framework import serializers

from vocab.exceptions import InternalError

from entries.models import Entry
from definitions.serializers import DefinitionSerializer

class EntrySerializer(serializers.ModelSerializer):
    definitions = DefinitionSerializer(many=True, read_only=True)

    class Meta:
        model = Entry
        fields = (
            'id',
            'word',
            'definitions',
            'created_date'
        )

    def create(self, validated_data):
        request = self.context.get('request', None)
        if not request:
            raise InternalError
        validated_data['owner'] = request.user
        return Entry.objects.create(**validated_data)
