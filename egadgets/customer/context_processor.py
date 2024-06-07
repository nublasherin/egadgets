from account.models import cart,orders

def cart_count(request):
    if request.user.is_authenticated:


       count=cart.objects.filter(user=request.user).count()
       return{"count":count}
    else:
        return {"count":0}

def order_count(request):
    if request.user.is_authenticated:
       co=orders.objects.filter(user=request.user).count()
       return{"add":co}
    else:
        return {"add":0}