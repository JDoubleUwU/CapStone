from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('HOME PAGE!')
    return render(request, 'base_generic.html', locals())