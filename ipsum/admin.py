from ipsum.models import Phrase
from django.contrib import admin


class PhraseAdmin(admin.ModelAdmin):
    list_display = ('phrase', 'create_dt', 'update_dt', 'approved')

admin.site.register(Phrase, PhraseAdmin)
