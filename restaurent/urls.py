from django.urls import path
from restaurent import views

urlpatterns = [
    
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login_view"),
    path("home", views.home, name="home"),
    path("register/", views.register, name="register"),
    path("adminpage/", views.admin, name="adminpage"),
    path("cashier/", views.cashier, name="cashier"),
    path("waiter/", views.waiter, name="waiter"),
    path("product/",views.product, name="product"),
    path("order/",views.order, name="order"),
    path("post_order/",views.post_order, name='post_order'),
    path("delete_order/<str:id>/",views.delete_order, name='delete_order'),
    path("update_order/<str:pk>/",views.update_order, name='update_order'),
    path("transaction/",views.transaction, name="transaction"),
    path("staff/",views.staff, name="staff"),
    path("post_product/",views.post_product, name='post_product'),
    path("delete_product/<str:id>/",views.delete_product, name='delete_product'),
    path("update_product/<str:pk>/",views.update_product, name='update_product'),
    path('delete_transaction/<str:id>',views.delete_transaction,name='delete_transaction'),
    path("update_transaction/<str:id>/",views.update_transaction,name="update_transaction")

]
