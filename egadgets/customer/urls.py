from django.urls import path
from .views import homeView,productView,DetailsView,addtoCart,cartListView,DeleteCart,checkOutView,OrderListView,cancelOrder
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('hom',homeView.as_view(),name='home'),
    path('pro<str:cat>',productView.as_view(),name='pro'),
    path('det/<int:pid>',DetailsView.as_view(),name='det'),
    path('addtocart/<int:pid>',addtoCart,name='acart'),
    path('cartlist',cartListView.as_view(),name='clist'),
    path('recart/<int:id>',DeleteCart,name='recart'),
    path('checkout/<int:cid>',checkOutView.as_view(),name='cout'),
    path('order',OrderListView.as_view(),name='olist'),
    path('cancel/<int:oid>',cancelOrder,name='corder')
    
  
   
   
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)