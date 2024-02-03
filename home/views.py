from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import authenticate
from .models import RegisterForm
# Create your views here.
def login(request):
    return render(request,'login.html')

def homePg(request):
    return render(request,'home.html')
def registerform(request):
     if request.method == 'POST':
        
        
            fname = request.POST['fname']
            mname=request.POST['mname']  
            lname=request.POST['lname']  
            mno=request.POST['mno']  
            remail=request.POST['remail']  
            rpass=request.POST['rpass']  
            cpass=request.POST['cpass']  
            if(rpass==cpass):
                 
                reg=RegisterForm(Fname=fname,Mname=mname,Lname=lname,MobileNo=mno,Email=remail,Password=rpass)
            
                reg.save()
                return redirect('/login')

def loginform(request):
    if request.method == 'POST':
          remail=request.POST['remail'] 
          rpass=request.POST['rpass'] 
         
          chke=RegisterForm.objects.filter(Email=remail,Password=rpass).values()
          if chke is not None:
               return redirect('/')
          else:
               return redirect('/login')
          return render(request,'login.html',{'result1':chke}) 
        
    
          
     
            