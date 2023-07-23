from django.shortcuts import render
from django.http  import HttpResponse
# Create your views here.

def msd(request):
    return HttpResponse('msd is best cricketer')
