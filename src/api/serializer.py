from rest_framework import serializers


class OpenAISerializer(serializers.Serializer):
    text = serializers.CharField(max_length=10000,required=True)

