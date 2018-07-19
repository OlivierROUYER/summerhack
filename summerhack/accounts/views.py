from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from .form import ConnexionForm
from django.shortcuts import render, redirect
from accounts.merkelTree import mt
import datetime
from django.http import *
from accounts.models import Tree
from django.http import JsonResponse

"""
Fonction de connexion / login
"""


@csrf_exempt
def home(request):
    now = datetime.datetime.now()
    buffer1, buffer2 = "", ""
    mt_a = mt.MarkleTree('testA')
    buffer1 += "{}".format(mt_a.buffer)
    #buffer2 = mt.TestIfExist(mt_a)
    date = datetime.datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    return render(request, 'partials/home.html', locals())


def DisplayDatbase(request):
    try:
        #date = Tree.objects.all().lastest('created_at')
        tree_list = Tree.objects.all()
        tab = []
        for i in tree_list:
            tab.append({
                'created_at': i.created_at,
                'updated_at': i.updated_at,
                'folder_path': i.folder_path,
                'key': i.key,
            })
        return JsonResponse({'tree_list': tab}, content_type="application/json")
    except:
        return JsonResponse({'error': "Impossible de remplir le JSON"}, content_type="application/json")
