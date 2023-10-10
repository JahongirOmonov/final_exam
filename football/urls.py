from django.urls import path
from .views import GetAllField,CreateField,PatchField,GetAllReserve,CreateReserve,PatchReserve

urlpatterns=[
    #fields
    path('getallfield/',GetAllField.as_view()),
    path('createfield/',CreateField.as_view()),
    path('patchfield/',PatchField.as_view()),
    #reserves
    path('getallreserve/',GetAllReserve.as_view()),
    path('createreserve/',CreateReserve.as_view()),
    path('patchreserve/',PatchReserve.as_view())
    #searches
]
