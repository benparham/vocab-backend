from rest_framework import parsers, renderers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer

from vocab.serializers import UserSerializer

class TokenLogin(APIView):
    parser_classes = (parsers.JSONParser,)
    rebderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user)
        user_data = UserSerializer(user).data
        user_data['token'] = token.key
        return Response(user_data)
