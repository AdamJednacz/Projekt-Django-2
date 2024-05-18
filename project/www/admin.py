from django.contrib import admin
from .models import Industry,Offer,AcceptedOffer,Like , Unlike

admin.site.register(Industry)
admin.site.register(Offer)
admin.site.register(AcceptedOffer)
admin.site.register(Like)
admin.site.register(Unlike)