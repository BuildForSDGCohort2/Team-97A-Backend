from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, UserVerification
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',
                    'first_name', 'last_name', 'phone_number', 'address']

    fieldsets = (*UserAdmin.fieldsets,
                 (
                     'Other fields',
                     {
                         'fields': (
                             'phone_number', 'address'
                         ),
                     },
                 ),
                 )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserVerification)
