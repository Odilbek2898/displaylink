from django.shortcuts import render

from .models import Registration

def index(request):
    latest_bek_list = Registration.objects.order_by('-reg_date')[:5]
    return render(request, 'bek/list.html', {'latest_bek_list': latest_bek_list})

# def index(request,registration_UserName_id):
#     pass
#
