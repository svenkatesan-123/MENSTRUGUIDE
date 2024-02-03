from django.shortcuts import render

# Create your views here.
def nextPeriod(request):
    return render(request,'nextPeriod.html')

def ovulation(request):
    return render(request,'ovulation.html')

def pregnancyTracker(request):
    return render(request,'pregnancyTracker.html')