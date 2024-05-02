from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="Dreamtravel" ),
    path('about/',views.about,name="Dreamtravelabout" ),
    path('chatbot/',views.chatbot,name="Dreamtravelchatbot" ),
    path('login/',views.login,name="Dreamtravellogin" ),
    path('register/',views.registre,name="Dreamtravelregister" ),
    path('user-logout', views.user_logout,name='user-logout'),
    path('page/', views.page, name='page'),
]
