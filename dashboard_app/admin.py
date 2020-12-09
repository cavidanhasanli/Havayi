from django.contrib import admin
from dashboard_app.models import *
from django.core.mail import send_mail
from dashboard_app.models import BankList
from Havayi_Settings.settings import EMAIL_HOST_USER
from dashboard_app.signals import bank_send_mail

class BlankCreditAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'phone_number', 'amount', 'credit_type', 'send_user_num', 'otp_status', 'bank_id',)
    list_display_links = None
    list_editable = ('name_surname', 'phone_number', 'amount', 'credit_type', 'send_user_num', 'otp_status', 'bank_id')
    list_filter = ('name_surname', 'phone_number', 'amount', 'credit_type', 'send_user_num', 'otp_status', 'bank_id')
    change_form_template = 'admin/change_list.html'
    actions = ['send_invite']

    def send_invite(self, request, queryset):
        for email in queryset:
            email_filter = BankList.objects.get(bank_name=email.bank_id)

            bank_send_mail(sender=None,instance=email_filter.bank_email,created=None)

    send_invite.short_description = "Send invitation"


admin.site.register(BankList)
admin.site.register(BlankCredit, BlankCreditAdmin)
admin.site.register(CreditFields)
