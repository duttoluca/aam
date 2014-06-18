from django.contrib import admin

from ade.models import ADE_request, ADE_detail


class ADE_detailInline(admin.TabularInline):
    model = ADE_detail


class ADE_requestAdmin(admin.ModelAdmin):
    inlines = [
        #ADE_detailInline,
    ]

admin.site.register(ADE_request, ADE_requestAdmin)
