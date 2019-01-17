from django.shortcuts import render
from .models import Cafe
from .forms import CafeForm

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
    form = CafeForm()
    return render(request, 'main/write.html', {'form': form})

def cafelist(request):
    cafelistobj = Cafe.objects.all()
    if request.method == "POST":
        form = CafeForm(request.POST, request.FILES)
        if form.is_valid():
            cafe = form.save(commit=False)
            cafe.save()
            return render(request, 'main/cafedetails.html', {'cafeobj': cafe})
    return render(request, 'main/cafelist.html', {'cafelistobj':cafelistobj})

def cafedetails(request, pk):
    cafeobj = Cafe.objects.get(pk=pk)
    return render(request, 'main/cafedetails.html', {'cafeobj':cafeobj})

