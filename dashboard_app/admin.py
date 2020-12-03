from django.contrib import admin
from dashboard_app.models import *


class BlankCreditAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'phone_number', 'amount', 'credit_type', 'send_user_num', 'otp_status','bank_id',)
    list_display_links = None
    list_editable = ('name', 'surname', 'phone_number', 'amount', 'credit_type','send_user_num','otp_status','bank_id')
    list_filter = ('name', 'surname', 'phone_number', 'amount', 'credit_type','send_user_num','otp_status','bank_id')


admin.site.register(BankList)
admin.site.register(BlankCredit, BlankCreditAdmin)
admin.site.register(CreditFields)
