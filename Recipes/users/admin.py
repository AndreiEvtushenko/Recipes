from django.contrib import admin
from users.models import CustomUser

admin.site.register(CustomUser)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'surname',
        'username',
        'email',
        'telegram',
        'image',
    )
    list_editable = ('name',)
    search_fields = ('username',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
