from cmath import log
from tkinter import E
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login , logout
from django.http import HttpResponseRedirect,HttpResponse
# Create your views here.
from .models import Profile
from home.models import RegisterForm


def login_page(request):
    return render(request,'login.html')
    
    # if request.method == 'POST':
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     user_obj = User.objects.filter(username = email)

    #     if not user_obj.exists():
    #         messages.warning(request, 'Account not found.')
    #         return HttpResponseRedirect(request.path_info)


    #     if not user_obj[0].profile.is_email_verified:
    #         messages.warning(request, 'Your account is not verified.')
    #         return HttpResponseRedirect(request.path_info)

    #     user = authenticate(username = email , password= password)
    #     if user:
    #         if user.is_active:
    #             login(request , user)
    #             return redirect('/homeRemedies')

        

    #     messages.warning(request, 'Invalid credentials')
    #     return HttpResponseRedirect(request.path_info)


    # return render(request ,'login.html')


def register_page(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = email)

        if user_obj.exists():
            messages.warning(request, 'Email is already taken.')
            return HttpResponseRedirect(request.path_info)

        print(email)

        user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
        user_obj.set_password(password)
        user_obj.save()

        messages.success(request, 'An email has been sent on your mail.')
        return HttpResponseRedirect(request.path_info)


    return render(request ,'login.html')




def activate_email(request , email_token):
    try:
        user = Profile.objects.get(email_token= email_token)
        user.is_email_verified = True
        user.save()
        return redirect('/')
    except Exception as e:
        return HttpResponse('Invalid Email token')
    

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
          user_obj = User.objects.filter(username = remail)

          if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return HttpResponseRedirect(request.path_info)


          if not user_obj[0].profile.is_email_verified:
            messages.warning(request, 'Your account is not verified.')
            return HttpResponseRedirect(request.path_info)

          user = authenticate(username = remail , password= rpass)
          if user:
            login(request , user)
            return redirect('/homeRemedies')

        

          messages.warning(request, 'Invalid credentials')
          return HttpResponseRedirect(request.path_info)


    return redirect('/') 
         
        #   chke=RegisterForm.objects.filter(Email=remail,Password=rpass).values()
        #   if chke is not None:
        #        return redirect('/login')
        #   else:
        #        return redirect('/login')
        #   return render(request,'login.html',{'result1':chke}) 
        
    
          
     
            


    
