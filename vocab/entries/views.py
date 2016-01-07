from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from entries.models import Entry
from entries.serializers import EntrySerializer

class EntryViewSet(viewsets.ModelViewSet):
    serializer_class = EntrySerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Entry.objects.filter(owner=user)

    def create(self, request):
        # serializer = ProjectSerializer(data=request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
