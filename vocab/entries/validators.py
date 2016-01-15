from rest_framework.serializers import ValidationError

def valid_word(value):
    if (not value.isalpha()):
        raise ValidationError('Word must be alphabetic')
