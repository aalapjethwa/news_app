from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from users.models import AppUser
User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):
    pass


class AppUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'get_categories')
    fields = (
        'first_name', 'last_name','username', 'email', 'categories'
    )

    def get_categories(self, obj):
        return list(obj.categories.values_list('name', flat=True))
    get_categories.short_description = "Categories"

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(is_staff=True, is_superuser=False)



admin.site.register(AppUser, AppUserAdmin)
