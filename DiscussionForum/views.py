from django.shortcuts import render
from django.shortcuts import redirect
from .models import DiscussionForum
# Create your views here.

def DiscussionForm(request):
    vari=DiscussionForum.objects.all().order_by('-id')[:10]
   

    if request.method == 'POST':
         
        
        chk=request.POST['btn']

        if(chk=='post'):
            try:
                data=request.session['hola']
                title = request.POST['title']
                dis=request.POST['desc']  
                reg=DiscussionForum(Distitle=title,DisDesc=dis)
            
                reg.save()
                return redirect('/')
            except:
                return redirect('/discussionForum')

        else:
           sear=request.POST['searchbar']
           vari=DiscussionForum.objects.filter(Distitle__icontains=sear).values() 
           try:
                return render(request,'discussionForum.html',{'result1':vari,'re':request.session['hola']}) 
           except:
               return render(request,'discussionForum.html',{'result1':vari}) 
        
           
        #    reg=DiscussionForum(Distitle=sear)
        #    reg.save()
    try:
        return render(request,'discussionForum.html',{'result1':vari,'re':request.session['hola']}) 
    except:
        return render(request,'discussionForum.html',{'result1':vari}) 
    
def DiscussionData(request):
    query = request.GET.get('query_name')
    iddata=DiscussionForum.objects.filter(id=query)
    try:
       return render(request,'data.html',{'result1':iddata,'re':request.session['hola']}) 
    except:
         return render(request,'data.html',{'result1':iddata})   
            
    
    


        
       
         
     
    return render(request,'index.html') 