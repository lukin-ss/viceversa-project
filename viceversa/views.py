from django.http import HttpResponse
from django.shortcuts import render


# def home(request):
#     return HttpResponse('This is home page')
#
#
# def home(request):
#     return HttpResponse('<h1>This is home page</h1>')


def home(request):
    return render(request, 'home.html')
