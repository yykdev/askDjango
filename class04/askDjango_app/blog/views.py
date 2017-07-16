from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def blog_index(request):
    return HttpResponse('Hello Blog Main !!!')


def post_list(reqeust):
    return HttpResponse('Hello Post List !!!')
