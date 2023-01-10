from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.


def index(request):
    return render(request, "login.html")


def register(request):
    msg = None
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = "user created"
            return redirect("login_view")
        else:
            msg = "form is not valid"
    else:
        form = SignUpForm()
    return render(request, "register.html", {"form": form, "msg": msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect("adminpage")
            elif user is not None and user.is_cashier:
                login(request, user)
                return redirect("cashier")
            elif user is not None and user.is_waiter:
                login(request, user)
                return redirect("waiter")
            else:
                msg = "invalid credentials"
        else:
            msg = "error validating form"
    return render(request, "login.html", {"form": form, "msg": msg})



def admin(request):
    return render(request, "adminsite/index.html")

def home(request):
    return render(request, "adminsite/index.html")

def cashier(request):
    return render(request, "cashiersite/cashier.html")


def waiter(request):
    return render(request, "waiter.html")

#region Product

def product(request):
    form = FormProduct()
    
    all = Product.objects.all()    
    context = {
        "all":all,
        "form":form
    }
    return render(request,"adminsite/products.html", context)

def post_product(request):
    form = FormProduct()
    if request.method == 'POST':
        # pname = request.POST.get('product_name')
        # cost = request.POST.get('cost')
        # date = request.POST.get('date')
        # product = Product(product_name = pname, product_cost=cost,created_at=date)
        form = FormProduct(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            pname = product.product_name
            # print(pname)
            product.save()
        # form = FormProduct(request.POST)
        
  
    return redirect('product')

def delete_product(request, id):
    product = Product.objects.get(id=id).delete()
    return redirect('product')

def update_product(request, pk):
    form = FormProduct()
    product = Product.objects.get(id=pk)
    form = FormProduct(instance=product)
    if request.method == 'POST':
        form = FormProduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')
    context = {
        "form":form
    }

    return render(request, 'update.html', context)

#endregion



#region Order

def order(request):
    form = OrderForm()
    all = Product.objects.all()  
    order = Order.objects.filter(status='process').all()
    context ={
        "all":all,
        "order":order,
        "form":form
    }
    return render(request, "adminsite/order.html", context)

def post_order(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            product = Product.objects.get(id=order.product_id)
            price = product.product_cost
            total_price = order.quantity*price
            print(total_price)
            trans = Transaction(order_id=order, total_price=total_price, payment_status='P' )
           
            trans.save()
            return redirect('order')
        else:
            print("invalid")
        print(form)



        # form = OrderForm(request.POST)
        # if form.is_valid():
        #     order = form.save(commit=False)
        #     oid = order.product_id
        #     quantity = order.quantity
        #     print(oid,quantity)
        #     order.save()
        # # form = FormProduct(request.POST)
        
  
    # return redirect('order')

def delete_order(request, id):
    order = Order.objects.get(id=id).delete()
    return redirect('order')

def update_order(request, pk):
    form = OrderForm()
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order')
    context = {
        "form":form
    }

    return render(request, 'update.html', context)

#endregion





def staff(request):
    context = {}
    return render(request, "adminsite/staff.html", context)


def transaction(request):
    trans = Transaction.objects.all()
    context = {
        "trans":trans
    }
    return render(request,"adminsite/transaction.html", context)




def delete_transaction(request, id):
    trans = Transaction.objects.get(id = id).delete()
    return redirect('transaction')


def update_transaction(request,id):
    return render (request,"adminsite/update_transaction.html")
    