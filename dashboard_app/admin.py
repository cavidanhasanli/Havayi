from django.contrib import admin
from dashboard_app.models import *
from dashboard_app.models import BankList, BlankCredit
from dashboard_app.signals import bank_send_mail


class BlankCreditAdmin(admin.ModelAdmin):
    list_display = ('name_surname', 'phone_number', 'amount', 'credit_type', 'send_user_num','otp_status', 'bank_id')
    list_display_links = None
    list_editable = ('bank_id',)
    list_filter = ('name_surname', 'phone_number', 'amount', 'credit_type', 'send_user_num', 'otp_status', 'bank_id')
    change_form_template = 'admin/change_list.html'
    actions = ['send_invite']

    # def bank_names(self, obj):
    #     print('ssssssssssssss', obj.credit_type)
    #     bank_filter = BankList.objects.filter(credit_type__credit_name=obj.credit_type)
    #     bank_list = []
    #     for i in bank_filter:
    #         if i.interest != 0.0:
    #             bank_list.append(i.bank_name)
    #     print(bank_list)
    #     return bank_list

    def has_add_permission(self, request):
        return False

    def send_invite(self, request, queryset):
        for email in queryset:

            bank_send_mail(sender=None, instance=email, created=None)

    send_invite.short_description = "Send invitation"


class BankListAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'bank_email', 'credit_type', 'interest',)
    list_display_links = None
    list_editable = ('bank_name', 'bank_email', 'credit_type', 'interest',)
    list_filter = ('bank_name', 'bank_email', 'credit_type', 'interest',)


admin.site.register(BankList, BankListAdmin)
admin.site.register(BlankCredit, BlankCreditAdmin)
admin.site.register(CreditFields)
