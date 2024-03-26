from django.contrib import admin
from .models import EmailModel

@admin.register(EmailModel)
class EmailModelAdmin(admin.ModelAdmin):

    list_display = [
        'id', 'email'
    ]
