from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Dreamtravel" ),
    path('about/',views.about,name="Dreamtravelabout" ),
    path('chatbot/',views.chatbot,name="Dreamtravelchatbot" ),
]
