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
    # return render(request, 'home.html', {'greeting': 'Hello!'})


def reverse(request):
    vvreview_text = request.GET['vvreview']
    print(vvreview_text)
    reversed_text = vvreview_text[::-1]
    word_count = len(vvreview_text.split())
    return render(request, 'reverse.html', {
        'vvreview': vvreview_text,
        'reversedtext': reversed_text,
        'wordcount': word_count
    })
