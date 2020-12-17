from django.contrib import admin
from .models import BankFiles
from .forms import ShowAdminForm
import csv
from user_app.models import *
from django.contrib import messages
from dashboard_app.models import *

admin.site.register(HavayiCashBack)


@admin.register(BankFiles)
class ShowAdmin(admin.ModelAdmin):
    form = ShowAdminForm
    actions = ['send_user_cashback']

    def send_user_cashback(self, request, queryset):
        csv_reader(queryset,request)
    send_user_cashback.short_description = "Send user cashback"

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        form.save_photos(form.instance)


def csv_reader(files,request):
    for f in files:
        with open(f'media/{f}', newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                if row['Status']:
                    bank_filter = BankList.objects.filter(bank_name=row['Bank']).filter(credit_type__credit_name=row['Kreditin növü'])

                    for num in bank_filter:

                        h = float(row['Təsdiqlənmiş kredit məbləği']) * num.interest / 2

                        if row['ID'] == '0':
                            print(h)
                        else:
                            user_cashback = MyUser.objects.get(MY_USER_ID=str(row['ID']))
                            user_cashback.cash_back = user_cashback.cash_back + float(h)
                            user_cashback.save()

                else:
                    messages.error(request,f'{f} Bu faylda Status qeyd olunmayib')