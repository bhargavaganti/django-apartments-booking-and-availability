__author__ = 'wojtek'
from modeltranslation.translator import translator, TranslationOptions
from offers.models import Offer,Offers

class OffersTranslationOptions(TranslationOptions):
    fields = ('title','text')

class OfferTranslationOptions(TranslationOptions):
    fields = ('title','price', 'text')

translator.register(Offer,OfferTranslationOptions)
translator.register(Offers,OffersTranslationOptions)