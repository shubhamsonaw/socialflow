from rest_framework import serializers


class ScrapeURLSerializer(serializers.Serializer):
    url = serializers.URLField()