from django.contrib import admin

# Register your models here.
from .models import client , projects , User


class clientAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_info' ,'get_project_name']
    def get_project_name(self , obj):
        return ', '.join([project.pname for project in obj.projects.all()])
    get_project_name.short_description = 'Projects'
    ordering = ['id']
class projectAdmin(admin.ModelAdmin):
    list_display = ['pname', 'client' , 'get_users']

    def get_users(self , obj):
        return ', '.join([user.userName for user in obj.users.all()])
    get_users.short_description = 'User'
    ordering = ['id']
    

class UserAdmin(admin.ModelAdmin):
    list_display = ['userName' , 'email' , 'isActive']
    ordering =['id']



admin.site.register(client, clientAdmin)
admin.site.register(projects ,projectAdmin )
admin.site.register(User ,UserAdmin)

