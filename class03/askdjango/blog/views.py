from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def post_list(request):
    return render(request, 'blog/post_list.html')


#def my_sum(request, x, y=0, z=0):
def my_sum(request, numbers):
    print(numbers)
    result = sum( int(number or 0) for number in numbers.split("/") )
    return HttpResponse(result)
