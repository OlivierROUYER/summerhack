from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .form import ConnexionForm
from django.shortcuts import render, redirect
from accounts.merkelTree import mt
import datetime
import os
"""
    Fonction de connexion / login
    """

#@csrf_exempt
#def login_user(request):
#    try:
#        if request.method == 'POST':
#            form = ConnexionForm(data=request.POST)
#            if form.is_valid():
#                form.clean()
#                user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
#                print(user)
#                if user is not None:
#                    login(request, user)
#                    return HttpResponseRedirect('/UserInfo/%s/' % user.id)
#        else:
#            form = ConnexionForm()
#    except Exception:
#        form = ConnexionForm()
#        print("Error login_user")
#    return render(request, 'registration/login.html', locals())


#@csrf_exempt
#def home(request):
#    return render(request, 'partials/home.html')


@csrf_exempt
def home(request):
    now = datetime.datetime.now()
    buffer1, buffer2 = "", ""
    mt_a = mt.MarkleTree('testA')
    # print(mt_a._mt)
    mt_b = mt.MarkleTree('testB')
    buffer1 += "{}{}".format(mt_a.buffer, mt_b.buffer)
    buffer2 += mt.MTDiff(mt_a, mt_a._tophash, mt_b, mt_b._tophash)
    date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M")
    print(buffer1, buffer2)
    return render(request, 'partials/home.html', locals())
