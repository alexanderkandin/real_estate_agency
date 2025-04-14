from django.contrib import admin

from .models import Flat, Complaints

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('owner','town','address','owners_phonenumber')
    list_display = ('address','price','new_building','construction_year','town','owner_pure_phone')
    list_editable = ('new_building',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building','rooms_number','has_balcony')
    raw_id_fields = ('likes',)


class ComplaintsAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat','user')

admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaints, ComplaintsAdmin)