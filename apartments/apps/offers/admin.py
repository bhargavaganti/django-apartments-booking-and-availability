from django.contrib import admin

from adminsortable.admin import SortableAdmin, SortableStackedInline
from .models import Offer, Offers

class Offer(SortableStackedInline):
    model = Offer
    extra = 1

class OffersAdmin(SortableAdmin):
    inlines = (Offer,)

admin.site.register(Offers, OffersAdmin)
