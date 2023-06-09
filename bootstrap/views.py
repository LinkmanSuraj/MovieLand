from django.http import HttpResponse
from django.shortcuts import redirect,render
from cards.models import movieCards
from webseries.models import webcards
from lastest.models import latestCards
def home(request):
    c_data=movieCards.objects.all()
    if request.method=="GET":
        mt=request.GET.get('search')
        if mt!=None:
             c_data=movieCards.objects.filter(title=mt)
    data={
        'c_data':c_data
    }
    return render(request,'/templates/index.html',data)

def feature(request):
    
    w_data=webcards.objects.all()
    if request.method=="GET":
        mt=request.GET.get('search')
        if mt!=None:
            w_data=webcards.objects.filter(w_title=mt)
    data={
        'w_data':w_data
    }
    return render(request,'Feature.html',data)

def price(request):
    
    l_data=latestCards.objects.all()
    if request.method=="GET":
        mt=request.GET.get('search')
        if mt!=None:
            l_data=latestCards.objects.filter(l_title=mt)
    data={
        'l_data':l_data
    }

    return render(request,'price.html',data)

