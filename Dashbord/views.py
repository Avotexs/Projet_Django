from django.shortcuts import render , HttpResponse , redirect
from .formes import CreateUserForm, LoginForm
from  django.contrib.auth.models import auth
from  django.contrib.auth import authenticate, login, logout

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

def login(request):
    form = LoginForm()  # Instantiate the LoginForm class
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Populate the form with POST data
        if form.is_valid():
            username = form.cleaned_data.get('username')  # Retrieve cleaned data from the form
            password = form.cleaned_data.get('password')
            # Your authentication logic here
            return redirect("/about/")  # Redirect to appropriate page after successful login
    return render(request, 'Dashbord/login.html', {'title': 'Login', 'loginform': form})




def registre(request):
   form = CreateUserForm()
   if request.method=="POST":
          form=CreateUserForm(request.POST)


          if form.is_valid():
                form.save()

                return redirect("/login/")

   context = {'registerform':form, 'title':'registred'}
   return render(request,'Dashbord/register.html',context=context)


def  user_logout(request):
    auth.logout(request)
    return redirect("Dreamtravellogin")

def page(request):
    # Logique pour gérer les actions de l'utilisateur (ajouter une photo, modifier les paramètres, etc.)
    return render(request, 'Dashbord/page.html', {'title': 'Page'})