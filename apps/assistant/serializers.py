from rest_framework import serializers


class ChatSerializer(serializers.Serializer):
    message = serializers.CharField()
    
class AssistantSerializer(serializers.Serializer):

    intent = serializers.CharField()
    topic = serializers.CharField(required=False)