from django.contrib import admin
from .models import BankFiles
from .forms import ShowAdminForm


@admin.register(BankFiles)
class ShowAdmin(admin.ModelAdmin):
    form = ShowAdminForm

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)
