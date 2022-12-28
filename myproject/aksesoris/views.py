from django.shortcuts import render
from .forms import aksesorisForms
from .models import aksesorisModel
# Create your views here.


def index(request):
    aksesorismodel = aksesorisModel.objects.all()
    context = {
        'title' : 'appaksesoris',
        'model': aksesorismodel

    }

    return render(request, 'aksesoris/aksesoris.html',context)




def index2(request):

    aksesorisforms = aksesorisForms()
    context = {
        'title' : 'appaksesoris',
        'form': aksesorisforms,

    }

    return render (request, 'aksesoris/aksesoris.html', context)