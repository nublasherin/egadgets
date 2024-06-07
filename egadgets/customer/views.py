from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.views import View
from django.views.generic import TemplateView,ListView,DetailView
from django.views import View
from account.models import product,cart,orders
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.core.mail import send_mail


#decorators
def signing_required(fn):
    def inner(request,*args,**kwargs):
        if request.user.is_authenticated:
            return fn(request,*args,**kwargs)
        else:
            messages.info(request,"please login first!!")
            return redirect('log')
    return inner

decorators=[signing_required,never_cache]

@method_decorator(decorators,name='dispatch')
class homeView(TemplateView):
    template_name="home.html"

# class productView(View):
#      def get(self,request,**kwargs):
#           cat=kwargs.get('cat')
#           print(cat)
#           data=product.objects.filter(category=cat)
#           print(data)
#           return render(request,"product.html")

@method_decorator(decorators,name='dispatch')
class productView(ListView):
    template_name="product.html"
    queryset=product.objects.all()
    context_object_name="data"
    def get_queryset(self) -> QuerySet[Any]:
         qs=super().get_queryset()
         qs=qs.filter(category=self.kwargs.get('cat'))
         return qs
    
@method_decorator(decorators,name='dispatch')
class DetailsView(DetailView):
    template_name="details.html"
    queryset=product.objects.all()
    pk_url_kwarg="pid"
    context_object_name="product"
decorators
def addtoCart(request,*args,**kwargs):
    try:
        user=request.user
        pid=kwargs.get('pid')
        Product=product.objects.get(id=pid)
        try:
            Cart=cart.objects.get(user=user,product=Product)
            Cart.quantity+=1
            Cart.save()
            messages.success(request,"product Quantity Updated")
            return redirect('home')
        except:
            cart.objects.create(user=user,product=Product)
            messages.success(request,"product Added to Cart!!")
            return redirect('home')
    except:
        messages.error(request,"Cart entry failed")
        return redirect('home')
    
@method_decorator(decorators,name='dispatch')
class cartListView(ListView):
    template_name="cartlist.html"
    queryset=cart.objects.all()
    context_object_name="cart"

    def get_queryset(self):
        qs= super().get_queryset()
        qs=qs.filter(user=self.request.user)
        return qs



@method_decorator(decorators,name='dispatch')
def DeleteCart(request,*args,**kwargs):
   try:
        cid=kwargs.get('id')
        Cart=cart.objects.get(id=cid)
        Cart.delete()
        messages.success(request,"cart item Removed!")
        return redirect('clist')
   except:
       messages.error(request,"something went worng!")
       return redirect('clist')
        
@method_decorator(decorators,name='dispatch')
class checkOutView(TemplateView):
    template_name="checkout.html"

    def post(self,request,*args,**kwargs):
        try:
            cid=kwargs.get('cid')
            Cart=cart.objects.get(id=cid)
            product=Cart.product
            user=Cart.user
            ph=request.POST.get('phone')
            addr=request.POST.get('address')
            orders.objects.create(product=product,user=user,phone=ph,address=addr)
            Cart.delete()
            messages.success(request,"order placed successfully!!")
            return redirect('clist')
        except Exception as e:
            print(e)
            messages.error("somthing went worng!! oder placing cancelled!!")
            return redirect('clist')
            


@method_decorator(decorators,name='dispatch')
class OrderListView(ListView):
    template_name='order.html'
    queryset=orders.objects.all()
    context_object_name="orders"
    def get_queryset(self):
       qs= super().get_queryset()
       qs=qs.filter(user=self.request.user)

       return qs
decorators
def cancelOrder(request,*args,**kwargs):
  try:
    oid=kwargs.get('oid')
    order=orders.objects.get(id=oid)
    subject="Order Cancelling Acknowledgment"
    msg=f"Your order for {order.product.title} is successfully cancelled!!"
    fr="nublasherin61@gamil.com"
    to_ad=[request.user.email]
    send_mail(subject,msg,fr,to_ad)
    order.delete()
    messages.success(request,"order cancelled!!")
    return redirect('olist')
  except Exception as e:
      messages.error(request,e)
      return redirect('olist')
      







