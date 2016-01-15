from rest_framework import serializers

from vocab.exceptions import InternalError

from entries.models import Entry
from entries.validators import valid_word
from definitions.serializers import DefinitionSerializer

class EntrySerializer(serializers.ModelSerializer):
    definitions = DefinitionSerializer(many=True, read_only=True)
    word = serializers.CharField(validators=[valid_word])

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

        raw_word = validated_data.get('word', None)
        if raw_word:
            validated_data['word'] = raw_word.lower()

        return Entry.objects.create(**validated_data)

    def update(self, instance, validated_data):
        raw_word = validated_data.get('word', None)
        if raw_word:
            validated_data['word'] = raw_word.lower()
        super(EntrySerializer, self).update(instance, validated_data)
