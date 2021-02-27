from django.contrib import admin
from .models import SentMessage
from training_center.benifits.models import Benifits
from training_center.career.models import Career
from training_center.healthcare.models import HealthCare
from training_center.familysupport.models import FamilySupport
from training_center.peer2peer.models import Peer2Peer
from training_center.transition.models import Transition


class BenifitsAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)

class HealthCareAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)

class CareerAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)

class FamilySupportAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)

class Peer2PeerAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)

class TransitionAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)



admin.site.register(Benifits,BenifitsAdmin)
admin.site.register(HealthCare,HealthCareAdmin)
admin.site.register(Career,CareerAdmin)
admin.site.register(FamilySupport,FamilySupportAdmin)
admin.site.register(Peer2Peer,Peer2PeerAdmin)
admin.site.register(Transition,TransitionAdmin)
# admin.site.register(SentMessage)
