from django.shortcuts import render
from .models import Cafe

def index(request):
    if request.method == "POST":
        #print(request)
        #print(request.POST.keys())
        
        keys = list(request.POST.keys())
        keys.remove('csrfmiddlewaretoken')
        #print(keys[0])
        
        cafelistobj = []
        cafelistobjall = Cafe.objects.all()
        #print(cafelistobj)
        #print(type(cafelistobj))
        #print(dir(cafelistobj))
    
        for key in keys:
            for cafelist in cafelistobjall:
                #print(cafelist['tag'], key, cafelist.tag == key)
                cafetag = list(cafelist.tag.values())
                print(cafetag[0]['name'], key, cafetag[0]['name'] == key)
                if cafetag[0]['name'] == key:
                    cafelistobj.append(cafelist)
        print(cafelistobj)
        return render(request, 'main/cafelist.html', {'cafelistobj':cafelistobj})
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def write(request):
    return render(request, 'main/write.html')

def cafelist(request):
    cafelistobj = Cafe.objects.all()
    return render(request, 'main/cafelist.html', {'cafelistobj':cafelistobj})

def cafedetails(request, pk):
    cafeobj = Cafe.objects.get(pk=pk)
    return render(request, 'main/cafedetails.html', {'cafeobj':cafeobj})

