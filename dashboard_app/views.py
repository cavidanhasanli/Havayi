from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse
from dashboard_app.models import CreditFields, BlankCredit
from user_app.models import MyUser


@login_required
def home(request):
    credit_fields = CreditFields.objects.all()
    context = {'credit_fields': credit_fields}
    return render(request, 'home.html', context)


def credit(request, slug):
    if request.method == 'POST':
        print(request.user.username)
        name = request.POST['name']
        surname = request.POST['surname']
        phone_number = request.POST['phone_number']
        amount = request.POST['amount']
        credit_type = slug
        user_id = MyUser.objects.get(username=request.user.username)
        BlankCredit.objects.create(user_id=user_id,
                                   name=name,
                                   surname=surname,
                                   phone_number=phone_number,
                                   amount=amount,
                                   credit_type=credit_type,
                                   send_user_num=user_id.MY_USER_ID)

    return render(request, 'credit_type.html')
