from rest_framework import serializers

from definitions.models import Definition

class DefinitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Definition
        fields = (
            'id',
            'text',
            'part_of_speech',
            'source',
            'rank'
        )
