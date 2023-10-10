from django.contrib import admin

# Register your models here.
from .models import FieldModel, ReserveModel

admin.site.register(FieldModel)
admin.site.register(ReserveModel)
