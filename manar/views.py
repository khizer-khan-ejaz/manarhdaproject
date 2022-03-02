from turtle import home
from django.shortcuts import render
from manar.models import Contact

# Create your views here.
def index(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject =request.POST['subject']
        message=request.POST['message']
        phone_number=request.POST['phone_number']

        
        
        
        home=Contact(name=name, email=email, content=subject,textmessage=message, phone_number=phone_number)
        home.save()

    return render( request,'manar\index.html')
     
def about(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject =request.POST['subject']
        message=request.POST['message']
        phone_number=request.POST['phone_number']

        
        
        
        home=Contact(name=name, email=email, content=subject,textmessage=message, phone_number=phone_number)
        home.save()
    return render(request,'manar\\RADIOLOGY.HTML')  

def operation(request):      
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject =request.POST['subject']
        message=request.POST['message']
        phone_number=request.POST['phone_number']

        
        
        
        home=Contact(name=name, email=email, content=subject,textmessage=message, phone_number=phone_number)
        home.save()
    return render(request, 'manar\\OPERATION.HTML')


def dialaysis(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject =request.POST['subject']
        message=request.POST['message']
        phone_number=request.POST['phone_number']

        
        
        
        home=Contact(name=name, email=email, content=subject,textmessage=message, phone_number=phone_number)
        home.save()     
    return render(request, 'manar\\dialaysis.html') 


def medical(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject =request.POST['subject']
        message=request.POST['message']
        phone_number=request.POST['phone_number']

        
        
        
        home=Contact(name=name, email=email, content=subject,textmessage=message, phone_number=phone_number)
        home.save()
    return render( request, 'manar\\medical.html')



def hotel(request): 
    if request.method=="POST":    
        name=request.POST['name']
        email=request.POST['email']
        subject =request.POST['subject']
        message=request.POST['message']
        phone_number=request.POST['phone_number']

        
        
        
        home=Contact(name=name, email=email, content=subject,textmessage=message, phone_number=phone_number)
        home.save()
    return render(request, 'manar\\hotalmanage.html')        