from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .form import ConnexionForm
from django.shortcuts import render, redirect
from accounts.merkelTree import mt
import datetime
from django.core.files.storage import FileSystemStorage
import os
"""
    Fonction de connexion / login
    """


@csrf_exempt
def home(request):
    now = datetime.datetime.now()
    buffer1, buffer2 = "", ""
    mt_a = mt.MarkleTree('testA')
    # print(mt_a._mt)
    mt_b = mt.MarkleTree('testB')
    buffer1 += "{}".format(mt_a.buffer)
    buffer2 += mt.MTDiff(mt_a, mt_a._tophash, mt_b, mt_b._tophash)
    date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    #print(buffer1, buffer2)
    return render(request, 'partials/home.html', locals())

