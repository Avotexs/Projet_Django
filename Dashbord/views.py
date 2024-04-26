from django.shortcuts import render , HttpResponse

Dashbord = [{
    'name' : "Dashboard",  
    'title':'metat', 
    'icon':"fa fa",
    'color':'bg-blue', 
},
{
    'name' : "Dashboard",  
    'title':'metat', 
    'icon':"fa fa",
    'color':'bg-blue', 
}
]
# Create your views here.
def home(request):
    context = {
        'Dashbord': Dashbord
    }
    return render(request,'Dashbord/home.html',context)
def about(request):
   
    return render(request,'Dashbord/about.html', {'title':'About Us'})

def chatbot(request):
   
    return render(request,'Dashbord/chatbot.html', {'title':'chatbot'})