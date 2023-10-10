from modeltranslation.translator import translator, TranslationOptions
from football.models import FieldModel,ReserveModel

class FieldTranslationOptions(TranslationOptions):
    fields = ('name', 'address','description')
    required_languages = ('uz','description')


translator.register(FieldModel, FieldTranslationOptions)