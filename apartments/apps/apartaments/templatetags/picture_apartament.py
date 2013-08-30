__author__ = 'wojtek'
from django import template
from apartaments.models import Apartament

register = template.Library()

@register.simple_tag
def picture(apartament, **kwargs):
    """
    template tag for geting picture of apartament
    """
    if (apartament == ""):
        return Apartament.objects.all()[0].teaserPicture
    return Apartament.objects.all().filter(pk = apartament)[0].teaserPicture