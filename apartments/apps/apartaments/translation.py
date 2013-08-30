__author__ = 'wojtek'
from modeltranslation.translator import translator, TranslationOptions
from apartaments.models import Apartament

class ApartamentTranslationOptions(TranslationOptions):
    fields = ('name','subtitle', 'priceLow', 'priceHigh', 'teaserText', 'description')

translator.register(Apartament,ApartamentTranslationOptions)