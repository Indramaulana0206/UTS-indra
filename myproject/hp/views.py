from django.shortcuts import render
from .models import post
from .forms import hp

# Create your views here.


def index(request):
    postingan = post.objects.all()
    percobaan = hp()
    context = {
        'Post' : postingan,
        'form' : percobaan,
    }
    if request.method == 'POST':
        context['title']= request.POST['title']
        context['body']= request.POST['body']
    else :
        print(request.POST)
    return render(request, 'hp/hp.html',context)

