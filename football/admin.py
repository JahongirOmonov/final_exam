from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import FieldModel,ReserveModel
from .forms import FieldForm

class FieldAdmin(admin.ModelAdmin):
    form=FieldForm
    list_display=('name',)
    search_fields=('name',)
   






# Register your models here.

admin.site.register(FieldModel, FieldAdmin)
admin.site.register(ReserveModel)