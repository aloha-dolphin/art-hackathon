from django.shortcuts import render
from .models import Areainfo
# Create your views here.

def home(request):
    context={}
    return render(request, 'firstapp/home.html', context)

def result(request):
    context={}
    if request.method == "POST":
        userinput = []

        for i in range(0, 56):
            value = request.POST.get('place'+str(i+1))
            if value == '' : value = 0
            else : value = int(value)
            userinput.append(value)

        # print(userinput)
        
        # output = 함수(userinput)
        idx = [1, 2, 3, 4, 5]
        pred = [1.1, 1.2, 1.3, 1.4, 1.5]
        result = []
        for i in range(5):
            obj = Areainfo.objects.get(pk = idx[i])
            pr = pred[i]
            result.append({'obj' : obj, 'pr' : pr})

        context['result'] = result
    return render(request, 'firstapp/result.html', context)