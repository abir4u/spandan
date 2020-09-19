from django.contrib import admin
from  .models import Destination,Testimonial,News
from django.contrib.auth.models import Group
from django.contrib import messages
# Register your models here.

class D(admin.ModelAdmin):
    def marked_up(modeladmin, request, queryset):
        queryset.update(marked='True')
    marked_up.short_description = " Add Post on the Website "

    def marked_off(modeladmin, request, queryset):
        queryset.update(marked='False')
    marked_off.short_description = " Remove Post from the Website "

    def offer_dest(modeladmin,request,queryset):
        count = queryset.update(offer='True')
        messages.info(request,'{} offer hasbeen added successfully' .format(count))
    offer_dest.short_description= " Add offer to "
    
    actions=[marked_off,marked_up,offer_dest]

    list_display=('name','desc','price','offer')
    list_filter= ('marked',)

admin.site.register(Testimonial)
admin.site.register(Destination,D)
admin.site.register(News)
admin.site.site_header = "Django Tutorials"
