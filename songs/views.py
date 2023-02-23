from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Song
from .serializers import SongSerializer
from albums.models import Album
from rest_framework.generics import ListCreateAPIView
from django.shortcuts import get_object_or_404


class SongView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = SongSerializer

    def get_queryset(self):
        return Song.objects.filter(album_id=self.kwargs[self.lookup_field])

    def perform_create(self, serializer):
        album = get_object_or_404(Album, pk=self.kwargs[self.lookup_field])
        return serializer.save(album=album)
