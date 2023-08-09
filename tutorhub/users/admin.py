from django.contrib import admin
from .models import NewUser
from django.contrib.auth.admin import UserAdmin

# UserConfig customizes the admin interface for the NewUser model.
class UserConfig(UserAdmin):

    # Ordering of user records in the admin interface.
    ordering = ['date_joined']

    # Displayed fields in the user list view.
    list_display = ('user_type','email','first_name','last_name','is_superuser', 'is_active')

    # Grouping fields in sections for the edit view.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username','first_name','last_name')}),
        ('Permissions', {'fields': ('is_superuser','is_active', 'is_staff')}),
    )

    # Configuration for adding a new user in the admin interface.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'user_type', 'password1', 'password2')}
            ),
    )

# Register the NewUser model with the customized admin configuration.
admin.site.register(NewUser,UserConfig)