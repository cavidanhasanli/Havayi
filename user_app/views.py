from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib import messages
from .models import *
import random
from profile_app.models import *

def home(request):
    context = {'title': 'Ana Səhifə'}
    print(BankFiles.objects.all())
    return render(request, 'home.html',context)


def login(request):
    context = {'title': 'Daxil ol'}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        users = MyUser.objects.filter(username=username)
        user = auth.authenticate(request, username=username, password=password)

        if users.exists():
            user_check = MyUser.objects.get(username=username)
            if user_check.is_phone_status:
                if user is not None:
                    auth.login(request, user)
                    return redirect('home')

                else:
                    messages.info(request, 'Invalid credentials')
                    return redirect('login')
            else:
                messages.info(request, 'Bele bir istifadeci yoxdur..')
                return redirect('login')
        else:
            messages.info(request, 'Bele bir istifadeci yoxdur..')
            return redirect('login')

    else:
        return render(request, 'login.html',context)


def register(request):
    context = {'title': 'Qeydiyyat'}
    if request.method == 'POST':
        user_name = request.POST['username']
        phone_number = request.POST['phone_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if MyUser.objects.filter(username=user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif MyUser.objects.filter(phone=phone_number).exists():
                messages.info(request, 'Phone Number Taken')
                return redirect('register')
            else:
                if phone_number[0:4] == "+994" and phone_number[5:].isdigit() and len(phone_number) == 13:
                    MyUser.objects.create(username=user_name, phone=phone_number, is_phone_status=False)

                    filter_user = MyUser.objects.get(username=user_name)

                    if not str(password1).isdigit() and len(password1) > 8:
                        filter_user.set_password(password1)
                        filter_user.MY_USER_ID = random.randint(999, 9999)
                        filter_user.save()
                        otp_code = otp_generator(phone_number)
                        PhoneOTP.objects.create(phone=phone_number, otp=otp_code)
                        return redirect('otp', phone_number)

                    else:
                        filter_user.delete()
                        messages.info(request, "password not matching!!!!!")
                        return redirect('register')


                else:
                    messages.info(request, "phone number not matching...(+994xxxxxxxxx)")
                    return redirect('register')

        else:
            messages.info(request, "password not matching!!!!")
            return redirect('register')

    else:
        return render(request, 'register.html',context)


def logout(request):
    auth.logout(request)
    return redirect('login')


def otp_views(request, phone_number):
    context = {'title': 'Otp code'}
    check = PhoneOTP.objects.get(phone=phone_number)
    user = MyUser.objects.get(phone=phone_number)
    if request.method == 'POST':
        otp_code = request.POST['otp']
        if len(otp_code) == 4 and str(otp_code).isdigit():
            if otp_code == check.otp:
                user.is_phone_status = True
                user.save()
                check.delete()
                return redirect('login')
            else:
                messages.info(request, "OTP code yanlisdir")
                return redirect('otp', phone_number)
        else:
            messages.info(request, "OTP code un yazilisi yanlisdir")
            return redirect('otp', phone_number)

    return render(request, 'otp.html',context)


def otp_generator(phone):
    """
    Bu funksiya random methodu vasitəsi ilə
    otp kodlar yaradır
    Argument:
    1)Phone number
    """
    if phone:
        key = random.randint(999, 9999)
        return key
    else:
        print('t')
        return False
