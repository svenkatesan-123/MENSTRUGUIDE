from django.shortcuts import render
from django.shortcuts import redirect
from .models import DiscussionForum
# Create your views here.

def DiscussionForm(request):
    vari=DiscussionForum.objects.all().order_by('-id')[:10]
   

    if request.method == 'POST':
        
        chk=request.POST['btn']
        if(chk=='post'):
            title = request.POST['title']
            dis=request.POST['desc']  
            reg=DiscussionForum(Distitle=title,DisDesc=dis)
            
            reg.save()
            return redirect('/')
        else:
           sear=request.POST['searchbar']
           vari=DiscussionForum.objects.filter(Distitle__icontains=sear).values() 
           return render(request,'discussionForum.html',{'result1':vari}) 
        #    reg=DiscussionForum(Distitle=sear)
        #    reg.save()
    return render(request,'discussionForum.html',{'result1':vari})
def DiscussionData(request):
    query = request.GET.get('query_name')
    iddata=DiscussionForum.objects.filter(id=query)
    return render(request,'data.html',{'result1':iddata}) 
        
            
        
    


        
       
         
     
    return render(request,'index.html') 