from annotations.models import WorldBorder
from rest_framework.utils import serializer_helpers
from .serializers import (
    WorldBorderSerializer
)
from rest_framework import (viewsets, generics, status)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


class WorldBorderVeiws(viewsets.GenericViewSet, generics.ListAPIView):
    serializer_class = WorldBorderSerializer
    permission_classes = [AllowAny]
    queryset = WorldBorder.objects.filter(name__icontains='indonesia')

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
