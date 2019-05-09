from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Wronka',
        'title': 'papapapap',
        'content': 'To samo co w temacie'
    },
    {
        'author': 'Wjtk',
        'title': 'tez papapapapa',
        'content': 'hmm, moze?'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'developer': 'kirsie'})



