from . import models, serializers

from rest_framework import viewsets, permissions


class ParentViewSet(viewsets.ModelViewSet):
    """Check to create images"""

    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ParentSerializer
    queryset = models.FileParent.objects.prefetch_related("child_parent")


class ChildViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    serializer_class = serializers.ChildSerializer
    queryset = models.Child.objects.all()
