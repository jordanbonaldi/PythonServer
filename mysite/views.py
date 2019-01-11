from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse

from . import storing

def index(request, name, time):
    storing.add(name, time)

    objs = {'toto': name}
    for keys in storing.hash:
        print(keys)
        print(storing.hash[keys])
    return JsonResponse(objs)

def get(request):
    for keys in storing.hash:
        print(keys)
        print(storing.hash[keys])
    return JsonResponse(storing.hash)
