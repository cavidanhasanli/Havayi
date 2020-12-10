from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from dashboard_app.models import CreditFields, BlankCredit
from user_app.models import MyUser, PhoneOTP
from django.contrib import messages
from user_app.views import otp_generator
import csv

 
@login_required
def credit_page(request):
    credit_fields = CreditFields.objects.all()
    context = {'credit_fields': credit_fields}
    return render(request, 'credit_page.html', context)


def credit(request, slug):
    if request.method == 'POST':
        print(request.user.username)
        name_surname = request.POST['name_surname']
        phone_number = request.POST['phone_number']
        amount = request.POST['amount']
        credit_type = slug
        user_id = MyUser.objects.get(username=request.user.username)

        if phone_number[0:4] == "+994" and phone_number[5:].isdigit() and len(phone_number) == 13:
            if amount:
                files = open(f'UserId:{user_id.MY_USER_ID}.csv', 'w',newline='')
                with files:
                    header = ['Ad/Soyad',
                              'Əlaqə Nömrə',
                              'Müraciət olunan kredit məbləği',
                              'ID',
                              'Təsdiqlənmiş kredit məbləği',
                              'Status',
                              'Kreditin növü',
                              'Bank']
                    writer = csv.DictWriter(files,fieldnames=header)
                    writer.writeheader()
                    writer.writerow({'Ad/Soyad':name_surname,
                                    'Əlaqə Nömrə':phone_number,
                                     'Müraciət olunan kredit məbləği':amount,
                                     'ID':user_id.MY_USER_ID,
                                     'Kreditin növü':credit_type,})

                BlankCredit.objects.create(user_id=user_id,
                                           name_surname=name_surname,
                                           phone_number=phone_number,
                                           amount=amount,
                                           credit_type=credit_type,
                                           send_user_num=user_id.MY_USER_ID,
                                           otp_status=False)
                otp_code = otp_generator(phone_number)
                PhoneOTP.objects.create(phone=phone_number, otp=otp_code)
                return redirect('otp_code', phone_number)

            else:

                # files = open(f'UserId:{user_id.MY_USER_ID}.csv', 'w', newline='')
                # with files:
                #     header = ['Ad/Soyad',
                #               'Əlaqə Nömrə',
                #               'Müraciət olunan kredit məbləği',
                #               'ID',
                #               'Təsdiqlənmiş kredit məbləği',
                #               'Status',
                #               'Kreditin növü',
                #               'Bank']
                #     writer = csv.DictWriter(files, fieldnames=header)
                #     writer.writeheader()
                #     writer.writerow({'Ad/Soyad': name_surname,
                #                      'Əlaqə Nömrə': phone_number,
                #                      'Müraciət olunan kredit məbləği': 1000,
                #                      'ID': user_id.MY_USER_ID,
                #                      'Kreditin növü': credit_type, })

                BlankCredit.objects.create(user_id=user_id,
                                           name_surname=name_surname,
                                           phone_number=phone_number,
                                           amount=1000,
                                           credit_type=credit_type,
                                           send_user_num=user_id.MY_USER_ID,
                                           otp_status=False)
                otp_code = otp_generator(phone_number)
                PhoneOTP.objects.create(phone=phone_number, otp=otp_code)
                return redirect('otp_code', phone_number)

        else:
            messages.info(request, "phone number not matching...(+994xxxxxxxxx)")
            return redirect('register')

    return render(request, 'credit_type.html')


def otp_views(request, phone_number):
    check = PhoneOTP.objects.get(phone=phone_number)
    otp_change_status = BlankCredit.objects.get(phone_number=phone_number)

    if request.method == 'POST':
        otp_code = request.POST['otp']

        if len(otp_code) == 4 and str(otp_code).isdigit():
            if otp_code == check.otp:
                otp_change_status.otp_status = True
                otp_change_status.save()
                check.delete()
                return redirect('credit_page')

            else:
                messages.info(request, "OTP code yanlisdir")
                return redirect('otp_code', phone_number)
        else:
            messages.info(request, "OTP code un yazilisi yanlisdir")
            return redirect('otp_code', phone_number)

    return render(request, 'otp_code.html')