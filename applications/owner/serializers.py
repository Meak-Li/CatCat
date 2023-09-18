from rest_framework import serializers

from applications.owner.models import Owner


class OwnerSerializer(serializers.Serializer):
    args = serializers.CharField(max_length=22)
