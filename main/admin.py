from django.contrib import admin
from .models import PortfolioItem, PortfolioItemGallery, ServiceItem, ServiceItemGallery, ServiceItemClients
from django.utils.translation import gettext_lazy as _


class PortfolioItemGalleryInline(admin.TabularInline):
    model = PortfolioItemGallery
    extra = 1


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    inlines = [PortfolioItemGalleryInline]
    list_display = ('name', 'category', 'project_date')
    list_display_links = ('name', 'category', 'project_date')
    list_filter = ('category',)
    date_hierarchy = 'project_date'
    fieldsets = (

        (_('PORTFOLIO ITEM'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ['name', 'category', 'image', 'project_date', 'project_url', 'client', 'description']
        }),
    )


class ServiceItemGalleryInline(admin.TabularInline):
    model = ServiceItemGallery
    extra = 1


class ServiceItemClientsInline(admin.TabularInline):
    model = ServiceItemClients
    extra = 1


@admin.register(ServiceItem)
class ServiceItemAdmin(admin.ModelAdmin):
    inlines = [ServiceItemGalleryInline, ServiceItemClientsInline]
    list_display = ('name', )
    list_display_links = ('name', )
    fieldsets = (

        (_('SERVICE ITEM'), {
            'classes': ('wide', 'extrapretty'),
            'fields': ['name', 'image', 'color', 'svg_path', 'data_aos_delay', 'description']
        }),
    )
