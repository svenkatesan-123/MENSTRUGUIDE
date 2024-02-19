from django.shortcuts import render

# Create your views here.
def nextPeriod(request):
    try:
       return render(request,'nextPeriod.html',{'re':request.session['hola']})
    except:
         return render(request,'nextPeriod.html')
    return render(request,'nextPeriod.html')

def ovulation(request):
    try:
       return render(request,'ovulation.html',{'re':request.session['hola']})
    except:
         return render(request,'ovulation.html')
    return render(request,'ovulation.html')

def pregnancyTracker(request):
    try:
       return render(request,'pregnancyTracker.html',{'re':request.session['hola']})
    except:
         return render(request,'pregnancyTracker.html')
    return render(request,'pregnancyTracker.html')