from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Post


def blog_index(request):
    return HttpResponse('Hello Blog Main !!!')


def post_list(request):
    qs = Post.objects.all()
    query = request.GET.get('query', '')
    if query:
        condition = Q(title__icontains=query) | Q(content__icontains=query)
        qs = qs.filter(condition)
    context = {
        'post_list': qs,
        'query': query,
    }
    return render(request, 'blog/post_list.html', context=context)
