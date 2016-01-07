from rest_framework import viewsets, permissions
from django.contrib.auth.models import User

from vocab.serializers import UserSerializer
from vocab.permissions import UserPermission

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (UserPermission,)
