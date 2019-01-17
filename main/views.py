from django.shortcuts import render
from main.models import Cafe

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def cafelist(request):
    cafelistobj = Cafe.objects.all()
    return render(request, 'main/cafelist.html', {'cafes':cafelistobj})

def cafedetails(request, pk):
    cafeobj = Cafe.objects.get(pk=pk)
    return render(request, 'main/cafedetails.html', {'cafe':cafeobj})