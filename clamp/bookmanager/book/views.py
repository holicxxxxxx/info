from django.shortcuts import render

# Create your views here.
from django.http import HttpRequest

from django.http import HttpResponse

def index(request):

    # return HttpResponse("ok")
    context={
        'name':'clamp'
    }

    return render(request,'book/index.html',context=context)