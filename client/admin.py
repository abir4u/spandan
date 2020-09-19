from django.contrib import admin
from django.db import models
from django.contrib.auth.models import Group
from  .models import posts,Comment
# Register your models here.
class postsAdmin(admin.ModelAdmin):
    list_display = ('post_name','post_marked')
admin.site.register(posts,postsAdmin)
class CommentAdmin(admin.ModelAdmin):

    

    def activate_comment(modeladmin, request, queryset):
        count = queryset.update(active ='True')
        messages.info(request,'{} offer has been active successfully' .format(count))
    activate_comment.short_description = " Activate Comments "

    def deactivate_comment(modeladmin, request, queryset):
        queryset.update(active ='False')
    deactivate_comment.short_description = " Deactivate Comments "

    actions = [activate_comment,deactivate_comment]
 
admin.site.register(Comment,CommentAdmin)

# class catagory_list(admin.ModelAdmin,qu):
#    travel = queryset(post_marked = 'True')
#    print(travel)
# admin.site.register(catagory_list)