from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _
from accounts.models import User


@admin.register(User)
class UserAdmin(DefaultUserAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_editable = ['is_staff', 'is_active']
    list_filter = ['gender', 'is_staff', 'is_superuser', 'is_active']
    # fieldsets=(
    #     ('Personal info ',{'fields':('first_name','last_name','email','gender','age','description')}),
    #     ('Contact info',{'fields':('phone','address')})

    # )
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'gender', 'age', 'description')}),
        (_('Contact info'), {'fields': ('phone', 'address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

