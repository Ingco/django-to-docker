from . import models

from rest_framework import serializers


class ChildSerializer(serializers.ModelSerializer):
    """models.Child Serializer"""

    class Meta:
        model = models.Child
        fields = ("id", "title", "parent")


class ParentSerializer(serializers.ModelSerializer):
    """models.ParentFile Serializer"""

    children = ChildSerializer(many=True, source="child_parent", read_only=True)

    class Meta:
        model = models.FileParent
        fields = ("id", "title", "children")
