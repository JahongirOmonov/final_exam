from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import FieldSerializer,ReserveSerializer
from .models import FieldModel,ReserveModel
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permission import OwnerPermissionClass,AdminPermissionClass,OwnerStadiumPermissionClass


#field
class GetAllField(generics.ListAPIView):
    queryset=FieldModel.objects.all()
    serializer_class=FieldSerializer
    permission_classes=(IsAuthenticated,)

class CreateField(generics.CreateAPIView):
    queryset=FieldModel.objects.all()
    serializer_class=FieldSerializer
    permission_classes=(IsAuthenticated,)

class PatchField(generics.RetrieveUpdateDestroyAPIView):
    queryset=FieldModel.objects.all()
    serializer_class=FieldSerializer
    permission_classes=(IsAuthenticated)

#reserve
class GetAllReserve(generics.ListAPIView):
    queryset=ReserveModel.objects.all()
    serializer_class=ReserveSerializer
    permission_classes=(IsAuthenticated,)

class CreateReserve(generics.CreateAPIView):
    queryset=ReserveModel.objects.all()
    serializer_class=ReserveSerializer
    permission_classes=(IsAuthenticated)

class PatchReserve(generics.RetrieveUpdateDestroyAPIView):
    queryset=ReserveModel.objects.all()
    serializer_class=ReserveSerializer
    permission_classes=(IsAuthenticated)
