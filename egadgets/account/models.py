from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class product(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    description=models.CharField(max_length=100)
    image=models.ImageField(upload_to="product_images")
    options=(("smart Phone","smart phone"),
             ("laptop","laptop"),
             ("tablates","tablates"),
             ("smartwatch","smartwatch")
    )

    category=models.CharField(max_length=200,choices=options)
    def __str__(self) -> str:
        return self.title


class cart(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateField(auto_now_add=True)
    quantity=models.IntegerField(default=1)
    status=models.CharField(max_length=200, default="added")
    @property
    def total_price(self):
        amount=self.product.price*self.quantity
        return amount



class orders(models.Model):
    product=models.ForeignKey(product,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    address=models.CharField(max_length=300)

    date=models.DateField(auto_now_add=True)
    option=(("order placed","order placed"),
          ("shipped","shipped"),
          ("out for delivery","out for delivery"),
          ("delivered","delivered"))
    status=models.CharField(max_length=200,default="order placed",choices=option)
    

