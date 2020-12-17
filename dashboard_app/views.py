from django.shortcuts import render, redirect
from dashboard_app.models import CreditFields, BlankCredit
from user_app.models import MyUser, PhoneOTP
from django.contrib import messages
from user_app.views import otp_generator


def credit_page(request):
    credit_fields = CreditFields.objects.all()
    context = {'credit_fields': credit_fields, 'title': 'Kreditlər'}
    return render(request, 'credit_page.html', context)


def credit(request, slug):
    context = {'title': f'Kredit {slug}'}

    if request.method == 'POST':

        name_surname = request.POST['name_surname']
        phone_number = request.POST['phone_number']
        amount = request.POST['amount']
        credit_type = slug

        try:
            user_id = MyUser.objects.get(username=request.user.username)
        except MyUser.DoesNotExist:
            user_id = None

        if BlankCredit.objects.filter(phone_number=phone_number):
            messages.info(request, 'Phone Number Taken')
            return redirect('credit',slug=slug)
        else:
            if phone_number[0:4] == "+994" and phone_number[5:].isdigit() and len(phone_number) == 13:
                if user_id:
                    if amount:
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
                    if amount:
                        BlankCredit.objects.create(user_id=user_id,
                                                   name_surname=name_surname,
                                                   phone_number=phone_number,
                                                   amount=amount,
                                                   credit_type=credit_type,
                                                   send_user_num='0',
                                                   otp_status=False)
                        otp_code = otp_generator(phone_number)
                        PhoneOTP.objects.create(phone=phone_number, otp=otp_code)
                        return redirect('otp_code', phone_number)

                    else:
                        BlankCredit.objects.create(user_id=user_id,
                                                   name_surname=name_surname,
                                                   phone_number=phone_number,
                                                   amount=1000,
                                                   credit_type=credit_type,
                                                   send_user_num='0',
                                                   otp_status=False)

                        otp_code = otp_generator(phone_number)
                        PhoneOTP.objects.create(phone=phone_number, otp=otp_code)
                        return redirect('otp_code', phone_number)

            else:
                messages.info(request, "phone number not matching...(+994xxxxxxxxx)")
                return redirect('register')

    return render(request, 'credit_type.html', context)


def otp_views(request, phone_number):
    context = {'title': 'Otp Code'}
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

    return render(request, 'otp_code.html', context)
