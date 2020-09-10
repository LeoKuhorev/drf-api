from django.shortcuts import render, HttpResponse


def home(request):
    return HttpResponse('Nothing here, go to api/v1 route.')
