from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Region,Province,District, CityMunicipality,Barangay,Purok,Address

class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('username', 'first_name','last_name')
    list_filter = ('username', 'first_name',)
    ordering = ('username',)
    list_display = ('username', 'first_name','middle_name','last_name',
                    'is_superuser','is_active', 'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'first_name','middle_name','last_name',)}),
        ('Permissions', {'fields': ('is_superuser','is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','middle_name','last_name', 'password1', 'password2',)}),
    )

admin.site.register(User,UserAdminConfig)

admin.site.register(Region)

admin.site.register(Province)

admin.site.register(District)

admin.site.register(CityMunicipality)

admin.site.register(Barangay)

admin.site.register(Purok)

admin.site.register(Address)
