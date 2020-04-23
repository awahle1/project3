from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("toSignUp", views.toSignUp_view, name="toSignUp"),
    path("signUp", views.signUp_view, name="signUp"),
    path("pizzaMenu", views.pizzaMenu_view, name="pizzaMenu"),
    path("pastaMenu", views.pastaMenu_view, name="pastaMenu"),
    path("subMenu", views.subMenu_view, name="subMenu"),
    path("saladMenu", views.saladMenu_view, name="saladMenu"),
<<<<<<< HEAD
    path("platterMenu", views.platterMenu_view, name="platterMenu")
=======
    path("platterMenu", views.platterMenu_view, name="platterMenu"),
    path("orderSicilian", views.orderSicilian_view, name="orderSicilian"),
    path("orderPizza", views.orderPizza_view, name="orderPizza"),
#    path("orderSub", views.orderSub_view, name="orderSub"),
#    path("orderPasta", views.orderPasta_view, name="orderPasta"),
#    path("orderSalad", views.orderSalad_view, name="orderSalad"),
#    path("orderPlatter", views.orderPlatter_view, name="orderPlatter"),
<<<<<<< HEAD
>>>>>>> parent of 29e7e98... All add to order buttons working
=======
>>>>>>> parent of 29e7e98... All add to order buttons working
]
