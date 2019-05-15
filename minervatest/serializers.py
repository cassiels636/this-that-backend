from rest_framework import serializers
from .models import This, That


class ThisSerializer(serializers.ModelSerializer):
    class Meta:
        model = This
        fields = ("name", )


class ThatSerializer(serializers.ModelSerializer):
    class Meta:
        model = That
        fields = ("name", )


class RandPairingSerializer(serializers.Serializer):
    this_name = serializers.CharField(max_length=255)
    that_name = serializers.CharField(max_length=255)

