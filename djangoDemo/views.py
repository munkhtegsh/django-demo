from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html')


def count(request):
    fulltext = request.GET['fulltext']
    count = {}
    text = fulltext.split(' ')
    length = len(text)
    for word in text:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    sortedWords = sorted(
        count.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {'fulltext': count, 'length': length, 'sortedWords': sortedWords})


def exercise(request):
    return render(request, 'exercise.html')
