from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("registration", views.registration, name="registration"),
    path("menu", views.menu, name="menu"),
    path("order", views.order, name="order"),
    path("login",views.login_view, name="login"),
    path("logout",views.logout_view, name="logout"),
    path("check_username", views.check_username, name = "check_username"),
    path("vs", views.vs, name="vs"),
    path("info", views.info, name="info"),
    path("<int:item_id>", views.cart, name = "cart"),
    path("large/<int:item_id>", views.large, name = "large"),
    path("extras", views.extras, name="extras"),
    path("cart", views.cart, name="cart"),
    path("remove", views.remove, name="remove"),
    path("confirm",views.confirm, name="confirm"),
    path("confirmremove",views.confirmremove, name="confirmremove"),
    path("placed",views.placed, name="placed"),
    path("kitchen",views.kitchen, name="kitchen"),
    path("collected",views.collected, name="collected"),
    path("payment",views.payment, name="payment"),
    path("charged", views.charged, name="charged")
]
