from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'username',
        'email',
        'telegram',
        'image',
    )
    list_editable = ('first_name',)
    search_fields = ('username',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
