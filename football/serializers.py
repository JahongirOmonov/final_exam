from rest_framework import serializers
from .models import ReserveModel,FieldModel

class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model=FieldModel
        fields=("__all__")

class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReserveModel
        fields=("__all__")