from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.

def MenstrualAwareness(request):
    try:
       return render(request,'MenstrualAwareness.html',{'re':request.session['hola']})
    except:
         return render(request,'MenstrualAwareness.html')
    return render(request,'MenstrualAwareness.html')

def absenceOfPeriods(request):
    try:
       return render(request,'absenceOfPeriods.html',{'re':request.session['hola']})
    except:
         return render(request,'absenceOfPeriods.html')
    return render(request,'absenceOfPeriods.html')

def acneBreakout(request):
    try:
       return render(request,'acneBreakout.html',{'re':request.session['hola']})
    except:
         return render(request,'acneBreakout.html')
    return render(request,'acneBreakout.html')

def adaptgoodskin(request):
    try:
       return render(request,'adaptgoodskin.html',{'re':request.session['hola']})
    except:
         return render(request,'adaptgoodskin.html')
    return render(request,'adaptgoodskin.html')

def anemia(request):
    try:
       return render(request,'anemia.html',{'re':request.session['hola']})
    except:
         return render(request,'anemia.html')
    return render(request,'anemia.html')

def bodyBreakouts(request):
    try:
       return render(request,'bodyBreakouts.html',{'re':request.session['hola']})
    except:
         return render(request,'bodyBreakouts.html')
    return render(request,'bodyBreakouts.html')

def contact(request):
    try:
       return render(request,'contact.html',{'re':request.session['hola']})
    except:
         return render(request,'contact.html')
    return render(request,'contact.html')

def doDont(request):
    try:
       return render(request,'doDont.html',{'re':request.session['hola']})
    except:
         return render(request,'doDont.html')
    return render(request,'doDont.html')

def dryness(request):
    try:
       return render(request,'dryness.html',{'re':request.session['hola']})
    except:
         return render(request,'dryness.html')
    return render(request,'dryness.html')

def hairchange(request):
    try:
       return render(request,'hairchange.html',{'re':request.session['hola']})
    except:
         return render(request,'hairchange.html')
    return render(request,'hairchange.html')

def healthyHair(request):
    try:
       return render(request,'healthyHair.html',{'re':request.session['hola']})
    except:
         return render(request,'healthyHair.html')
    return render(request,'healthyHair.html')

def homeRemedies(request):
    try:
       return render(request,'homeRemedies.html',{'re':request.session['hola']})
    except:
         return render(request,'homeRemedies.html')
    return render(request,'homeRemedies.html')

def hygiene(request):
    try:
       return render(request,'hygiene.html',{'re':request.session['hola']})
    except:
         return render(request,'hygiene.html')
    return render(request,'hygiene.html')

def irregularPeriods(request):
    try:
       return render(request,'irregularPeriods.html',{'re':request.session['hola']})
    except:
         return render(request,'irregularPeriods.html')
    return render(request,'irregularPeriods.html')

def lightPeriods(request):
    try:
       return render(request,'lightPeriods.html',{'re':request.session['hola']})
    except:
         return render(request,'lightPeriods.html')
    return render(request,'lightPeriods.html')

def menopause(request):
    try:
       return render(request,'menopause.html',{'re':request.session['hola']})
    except:
         return render(request,'menopause.html')
    return render(request,'menopause.html')

def menstrualPainHR(request):
    try:
       return render(request,'menstrualPainHR.html',{'re':request.session['hola']})
    except:
         return render(request,'menstrualPainHR.html')
    return render(request,'menstrualPainHR.html')

def oilyhair(request):
    try:
       return render(request,'oilyhair.html',{'re':request.session['hola']})
    except:
         return render(request,'oilyhair.html')
    return render(request,'oilyhair.html')

def overcomeDarkSpot(request):
    try:
       return render(request,'overcomeDarkSpot.html',{'re':request.session['hola']})
    except:
         return render(request,'overcomeDarkSpot.html')
    return render(request,'overcomeDarkSpot.html')

def overcomeDryness(request):
    try:
       return render(request,'overcomeDryness.html',{'re':request.session['hola']})
    except:
         return render(request,'overcomeDryness.html')
    return render(request,'overcomeDryness.html')

def premenstrual(request):
    try:
       return render(request,'premenstrual.html',{'re':request.session['hola']})
    except:
         return render(request,'premenstrual.html')
    return render(request,'premenstrual.html')

def protectSkin(request):
    try:
       return render(request,'protectSkin.html',{'re':request.session['hola']})
    except:
         return render(request,'protectSkin.html')
    return render(request,'protectSkin.html')

def rashes(request):
    try:
       return render(request,'rashes.html',{'re':request.session['hola']})
    except:
         return render(request,'rashes.html')
    return render(request,'rashes.html')

def sheddingOfHairs(request):
    try:
       return render(request,'sheddingOfHairs.html',{'re':request.session['hola']})
    except:
         return render(request,'sheddingOfHairs.html')
    return render(request,'sheddingOfHairs.html')

def skinChange(request):
    try:
       return render(request,'skinChange.html',{'re':request.session['hola']})
    except:
         return render(request,'skinChange.html')
    return render(request,'skinChange.html')

def skinProblems(request):
    try:
       return render(request,'skinProblems.html',{'re':request.session['hola']})
    except:
         return render(request,'skinProblems.html')
    return render(request,'skinProblems.html')

def vaginalInfectionsHR(request):
    try:
       return render(request,'vaginalInfectionsHR.html',{'re':request.session['hola']})
    except:
         return render(request,'vaginalInfectionsHR.html')
    return render(request,'vaginalInfectionsHR.html')

def vaginalItching(request):
    try:
       return render(request,'vaginalItching.html',{'re':request.session['hola']})
    except:
         return render(request,'vaginalItching.html')
    return render(request,'vaginalItching.html')

def whyacne(request):
    try:
       return render(request,'whyacne.html',{'re':request.session['hola']})
    except:
         return render(request,'whyacne.html')
    return render(request,'whyacne.html')

def whyacneoccurs(request):
    try:
       return render(request,'whyacneoccurs.html',{'re':request.session['hola']})
    except:
         return render(request,'whyacneoccurs.html')
    return render(request,'whyacneoccurs.html')

def whylate(request):
    try:
       return render(request,'whylate.html',{'re':request.session['hola']})
    except:
         return render(request,'whylate.html')
    return render(request,'whylate.html')

def yoga(request):
    try:
       return render(request,'yoga.html',{'re':request.session['hola']})
    except:
         return render(request,'yoga.html')
    return render(request,'yoga.html')
def quiz(request):
    try:
       return render(request,'quiz.html',{'re':request.session['hola']})
    except:
         return render(request,'quiz.html')
    return render(request,'quiz.html')