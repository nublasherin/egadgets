from django.urls import path
from .views import regView,LoginView,LogOut


urlpatterns = [
    path('log',LoginView.as_view(),name='log'),
    path('reg',regView.as_view(),name='reg'),
    path('lout',LogOut.as_view(),name='lout')
   
   
]
