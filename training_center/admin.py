from django.contrib import admin
from .models import TrainingCenter
from videos_app.models import Videos
from training_center.construction.models import Construction
from training_center.healthcare.models import HealthCare
from training_center.info_tech.models import InfoTech
from training_center.manufacturing.models import Manufacturing
from training_center.marketing.models import Marketing
from training_center.transportation.models import Transportation


class VideoInline(admin.StackedInline):
    model = Videos
    
class OutreachAndAdmissionAdmin(admin.ModelAdmin):
    inlines = [VideoInline]

class ConstructionAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)
class HealthCareAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)
class InfoTechAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)
class ManufacturingAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)
class MarketingAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)
class TransportationAdmin(admin.ModelAdmin):
    readonly_fields=('extra_field',)



admin.site.register(Construction,ConstructionAdmin)
admin.site.register(HealthCare,HealthCareAdmin)
admin.site.register(InfoTech,InfoTechAdmin)
admin.site.register(Manufacturing,ManufacturingAdmin)
admin.site.register(Marketing,MarketingAdmin)
admin.site.register(Transportation,TransportationAdmin)
