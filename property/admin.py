from django.contrib import admin

from .models import Flat, Complaints, Owner

class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ['owner',]

class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town','address',)
    list_display = ('address','price','new_building','construction_year','town',)
    list_editable = ('new_building',)
    readonly_fields = ('created_at',)
    list_filter = ('new_building','rooms_number','has_balcony',)
    raw_id_fields = ('likes',)
    inlines = [OwnerInline]


class ComplaintsAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat','user')


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',)



admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaints, ComplaintsAdmin)
admin.site.register(Owner, OwnerAdmin)