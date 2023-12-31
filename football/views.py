from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from django.http import HttpResponse, HttpRequest
from rest_framework.response import Response
from .serializers import FieldSerializer,ReserveSerializer
from .models import FieldModel,ReserveModel
from django.http import JsonResponse
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .permission import OwnerPermissionClass,AdminPermissionClass,OwnerStadiumPermissionClass,UserPermissionClass,AdminOrOwnerStadiumPermissionClass,AdminOrUserPermissionClass


#field
class GetAllField(generics.ListAPIView):
    queryset=FieldModel.objects.all()
    serializer_class=FieldSerializer
    permission_classes=(IsAuthenticated,)

class CreateField(generics.CreateAPIView):
    queryset=FieldModel.objects.all()
    serializer_class=FieldSerializer
    permission_classes=(IsAuthenticated,AdminOrOwnerStadiumPermissionClass)

class PatchField(generics.RetrieveUpdateDestroyAPIView):
    queryset=FieldModel.objects.all()
    serializer_class=FieldSerializer
    permission_classes=(IsAuthenticated,OwnerPermissionClass)

#reserve
class GetAllReserve(generics.ListAPIView):
    queryset=ReserveModel.objects.all()
    serializer_class=ReserveSerializer
    permission_classes=(IsAuthenticated,AdminOrOwnerStadiumPermissionClass)

class CreateReserve(generics.CreateAPIView):
    queryset=ReserveModel.objects.all()
    serializer_class=ReserveSerializer
    permission_classes=(IsAuthenticated,AdminOrUserPermissionClass)

class PatchReserve(generics.RetrieveUpdateDestroyAPIView):
    queryset=ReserveModel.objects.all()
    serializer_class=ReserveSerializer
    permission_classes=(IsAuthenticated,AdminOrOwnerStadiumPermissionClass)

#band bo`lmagan vaqtlarni ko`rsatadi
class UnReservedTime(APIView):
    def get(self, request, *args, **kwargs):
        detail=ReserveModel.objects.get(id=kwargs['forid'])
        return JsonResponse(f'00:00 - {detail.start_time} va {detail.end_time} - 23:59', safe=False)
