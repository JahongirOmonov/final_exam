from django.urls import path
from .views import GetAllField,CreateField,PatchField,GetAllReserve,CreateReserve,PatchReserve, UnReservedTime

urlpatterns=[
    #fields
    path('getallfield/',GetAllField.as_view()),
    path('createfield/',CreateField.as_view()),
    path('patchfield/<int:pk>',PatchField.as_view()),
    #reserves
    path('getallreserve/',GetAllReserve.as_view()),
    path('createreserve/',CreateReserve.as_view()),
    path('patchreserve/<int:pk>',PatchReserve.as_view()),
    #searches
    path('UnReservedTime/<int:forid>', UnReservedTime.as_view())
]
