from django.db import models
from django.contrib.auth.models import AbstractUser

"""
this class standars for table of database 
@TODO: register, display, updatade and delete.
and it holds for user authanication
e.g:name, email, phone, gender, role, username and password

"""


class User(AbstractUser):
    is_admin = models.BooleanField("Is admin",default=False)
    is_cashier = models.BooleanField("Is cashier",default=False)
    is_waiter = models.BooleanField("Is waiter",default=False)


"""
this class standars for table of database 
@TODO: register, display, updatade and delete.
and it holds for product details
e.g: product_name, product_cost, created_at

"""

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    product_cost = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name


"""
this class standars for table of database 
@TODO: register, display, updatade and delete.
and it holds for order throught customer 
e.g: procut id, user_id, quantity,total  price

"""

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=20, blank=True, null=True, default='process')

    def __str__(self):
        return f' {self.quantity} -- {self.product.product_name}'


"""
this class standars for table of database 
@TODO: register, display, updatade and delete.
and it holds for product details
e.g: payment_status, total_price, date, 

"""

class Transaction(models.Model):
    PAYMENT_STATUS_PENDING = 'P'
    PAYMENT_STATUS_COMPLETE = 'C'
    PAYMENT_STATUS_FAILED = 'F'


    PENDING_STATUS_CHOICES = [
        (PAYMENT_STATUS_PENDING, 'Pending'),
        (PAYMENT_STATUS_COMPLETE,'Complete'),
        (PAYMENT_STATUS_FAILED, 'Failed')
    ]


    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    total_price = models.IntegerField()

    payment_status = models.CharField(max_length=1, choices=PENDING_STATUS_CHOICES, default=PAYMENT_STATUS_PENDING )

    date = models.DateTimeField(auto_now=True)


    

