from rest_framework import serializers
from .models import ReserveModel,FieldModel
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model=FieldModel
        fields=("__all__")

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(FieldSerializer, self).create(validated_data)


class ReserveSerializer(serializers.ModelSerializer):
    class Meta:
        model=ReserveModel
        fields=("__all__")

    def create(self, validated_data):
        validated_data['user']=get_object_or_404(User, username=self.context['request'].user)
        return super(ReserveSerializer, self).create(validated_data)