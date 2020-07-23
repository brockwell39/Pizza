from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Avg, Sum
from.models import Fooditem, Catergory, Extras, Cart, Size, Order
from datetime import datetime, timedelta
from django.utils import timezone
import stripe

stripe.api_key = "sk_test_51H5A7wANnrfeh5rRNKAe6ddS6winJ1OAqRmxeDusrC9Ez2LWMeG5vlQgicPqkQOLMSj3qK2ZHZ6b87U0aIt32yrR0073cEv0TN"

from .forms import UserForm


# Create your views here.
def index(request):
    return render(request,"orders/index.html")

def vs(request):
    return render(request,"orders/vs.html")

def info(request):
    return render(request,"orders/info.html")


# if user removes from cart at confirm page
def confirmremove(request):
    if not request.user.is_authenticated:
        return redirect("order")
    cartitem = request.POST.__getitem__('remove')
    print(cartitem)
    tbd = Cart.objects.get(pk=cartitem)
    tbd.delete()
    return redirect("confirm")

def charged(request):
    if not request.user.is_authenticated:
        return redirect("order")
    user = request.user
    order = Order.objects.filter(user=user, complete=False, paid=False).last()
    amount = round((order.price)*100,0)
    if request.method == 'POST':
        stripe.Charge.create(
        amount = amount,
        currency ="usd",
        description = order.order,
        source = request.POST['stripeToken']
        )
    order.paid = True
    order.save()
    context = {
    "paid": order
    }
    return render(request,"orders/charged.html", context)

def payment(request):
    if not request.user.is_authenticated:
        return redirect("order")
    user = request.user
    order = Order.objects.filter(user=user, complete=False, paid=False).last()
    print(order)
    context = {
    "order": order
    }

    return render(request,"orders/payment.html",context)

# if user removes from cart on menu page
def remove(request):
    if not request.user.is_authenticated:
        return redirect("order")
    cartitem = request.POST.__getitem__('remove')
    print(cartitem)
    tbd = Cart.objects.get(pk=cartitem)
    tbd.delete()
    return redirect("order")

# updates order to complete when kitchen says
def collected(request):
    if not request.user.is_authenticated:
        return redirect("order")
    ordercomplete = request.POST.__getitem__('complete')
    cart = Order.objects.filter(order=ordercomplete)
    cart.update(complete=True)
    return redirect("kitchen")

# provides kitchen info
def kitchen(request):
    if request.user.is_superuser:
        x = Order.objects.values_list('order', flat=True)
        now = datetime.now()
        today = now.date()
        todays = Order.objects.filter(order_placed__gte = timezone.now() - timedelta(days=1))
        sales = Order.objects.filter(complete=True,order_placed__gte = timezone.now() - timedelta(days=1) ).aggregate(Sum('price'))
        if (sales['price__sum'] == None):
            total = 0
        else:
            total = round(sales['price__sum'],2)
        context = {
        "ordernos": Order.objects.values_list('order', flat=True).distinct(),
        "orders": Order.objects.filter(complete=False,order_placed__gte = timezone.now() - timedelta(days=1) ).order_by('requested'),
        "completed": Order.objects.filter(complete=True,order_placed__gte = timezone.now() - timedelta(days=1) ).order_by('requested'),
        "sales":total
        }
        return render(request, "orders/kitchen.html", context)
    else:
        return redirect("order")

# places order moves from cart to order model
def placed(request):
    # checks if user logged in
    if not request.user.is_authenticated:
        return redirect("order")
    user = request.user
    cart = Cart.objects.filter(user=user,ordered=False)
    lastorder = Order.objects.last()
    if lastorder is None:
        ordernumber = 1
    else:
        ordernumber = lastorder.order + 1;
    if "asap" in request.POST:
        now1 = timezone.now()
        now = datetime.now()
        time = now.strftime("%H:%M")
        print(time)
        for x in cart:
            price = x.price
            topings = x.toppings.all()
            o = Order(order=ordernumber,user=user, item=x.itemid, size=x.size,requested=time)
            o.save()
            extrap = 0
            for y in topings:
                extrap =+ y.price
                o.toppings.add(y)
                price = price + extrap
            o.price = price
            o.save()
            x.ordered = True
            x.save()
    elif "time" in request.POST:
        print("TIME")
        time = request.POST["time"]
        for x in cart:
            #item = Fooditem.objects.get(item=x.item)
            price = x.price
            topings = x.toppings.all()
            o = Order(order=ordernumber,user=user, item=x.itemid, size=x.size,asap=False,requested=time)
            o.save()
            extrap = 0
            for y in topings:
                extrap =+ y.price
                o.toppings.add(y)
                price = price + extrap
            o.price = price
            o.save()
            x.ordered = True
            x.save()
    if "online" in request.POST:
           return redirect("payment")
    else:
        message = "Order Placed"
        context = {
        "message" : message
        }
        return render(request,"orders/placed.html", context)

def confirm(request):
    # checks if user logged in
    if not request.user.is_authenticated:
        return redirect("order")
    user = request.user
    cart = Cart.objects.filter(user=user,ordered=False)
    # need to go through cart and check all toppings , if toppings not complete directs you to add toppings
    for i in cart:
        x = Fooditem.objects.get(pk=i.itemid.pk)
        if i.toppings.count() < (x.minnumberoftoppings):
            notop1 = i.pk
            notop = Cart.objects.get(pk=i.pk)
            notop.pk = None
            notop.save()
            i.delete()
            return redirect("extras")
    cart1 = Cart.objects.filter(user=user,ordered=False)
    total = Cart.objects.filter(user=user,ordered=False).aggregate(Sum('price'))
    total = total['price__sum']
    extrap = 0
    for x in cart1:
        topings = x.toppings.all()
        for y in topings:
            extrap = extrap + y.price
    if total is not None:
        total = total + extrap
        total = round(total,2)
    else:
        return redirect("order")
    context = {
        "cart" : cart1,
        "total" : total
    }
    return render(request,"orders/confirm.html", context)
# adds extras to items
def extras(request):
    if not request.user.is_authenticated:
        return redirect("order")
    if request.POST:
        topping = request.POST.__getitem__('topping')
        flavour = Extras.objects.get(id=topping)
        item = Cart.objects.last()
        food = Fooditem.objects.get(pk=item.itemid.pk)
        print("item",item.id)
        item.toppings.add(flavour)
    # if max no of toppings reached returns to order else lets add more maxnumberoftoppings
        if item.toppings.count() < (food.maxnumberoftoppings):
            return redirect("extras")
        else:
            return HttpResponseRedirect(reverse("order"))
    else:
        user = request.user
        # item is object in cart item1 is object in fooditems
        item = Cart.objects.last()
        item1 = Fooditem.objects.get(pk=item.itemid.pk)
        extras = Extras.objects.filter(canbeon=item1)
        message = ""
        #finds catergory of item and selectes appropriate topping messsage
        print(item1.cat)
        if str(item1.cat) == "Subs":
            message = "Would you like to add ?"
        elif str(item1.cat) == "Regular Pizza" or "Sicilian Pizza":
            toptochoose =(item1.minnumberoftoppings)-item.toppings.count()
            if toptochoose == 1:
                message = "Please choose "+str(toptochoose)+" more topping for your "+str(item1)
            else:
                message = "Please choose "+str(toptochoose)+" toppings for your "+str(item1)
        context = {
        "message":message,
        "cart": Cart.objects.filter(user=user,ordered=False),
        "extras":extras
            }
        return render(request,"orders/extras.html",context)

def cart(request, item_id):
    # checks if user logged in
    if not request.user.is_authenticated:
        return redirect("order")
    user = request.user
    item = Fooditem.objects.get(pk=item_id)
    small = Size.objects.get(size="Small")
    n = Cart(user=user, item=item.item, itemid=item, ordered=False, size=small, price=item.price)
    n.save()
    # if item has toppings gets toppings avail on item and sends user back to add extras page
    extras = Extras.objects.filter(canbeon=item)
    if len(extras) > 0 :
        return redirect("extras")
    # else adds item to cart and displays cart
    else:
        return redirect("order")
    return render(request,"orders/order.html",context)

def large(request, item_id):
    if not request.user.is_authenticated:
        return redirect("order")
    user = request.user
    item = Fooditem.objects.get(pk=item_id)
    large = Size.objects.get(size="Large")
    n = Cart(user=user, item=item.item,itemid=item,size=large,ordered=False, price=item.pricelarge)
    n.save()
    # if item has toppings gets toppings avail on item and sends user back to add extras page
    extras = Extras.objects.filter(canbeon=item)
    if len(extras) > 0 :
        return redirect("extras")
    # else adds item to cart and displays cart
    else:
        return redirect("order")

def order(request):
    if not request.user.is_authenticated:
        return redirect("menu")
    user = request.user
    total = Cart.objects.filter(user=user,ordered=False).aggregate(Sum('price'))
    total = total['price__sum']
    cart = Cart.objects.filter(user=user,ordered=False)
    # goes through cart and adds prices of all extras to total
    extrap = 0
    for x in cart:
        topings = x.toppings.all()
        for y in topings:
            extrap = extrap + y.price
    if total is not None:
        total = total + extrap
        total = round(total,2)
    else:
        total = 0
    context = {
    "items": Fooditem.objects.all(),
    "cats" : Catergory.objects.all(),
    "extras": Extras.objects.filter(price__exact=0),
    "user": user,
    "cart": cart,
    "total": total
    }
    return render(request,"orders/order.html",context)



def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password )
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("order"))
    else:
        context = {
        "items": Fooditem.objects.all(),
        "cats" : Catergory.objects.all(),
        "extras": Extras.objects.filter(price__exact=0),
        "message" : "Incorrect Password"
        }
        return render(request, "orders/menu.html", context)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("menu"))

def menu(request):
    if request.user.is_authenticated:
        return redirect("order")
    context = {
    "items": Fooditem.objects.all(),
    "cats" : Catergory.objects.all(),
    "extras": Extras.objects.filter(price__exact=0)
    }
    return render(request,"orders/menu.html",context)

def registration(request):
    form = UserForm()
    context = {
    "items": Fooditem.objects.all(),
    "cats" : Catergory.objects.all(),
    "extras": Extras.objects.filter(price__exact=0),
    'form': form
    }
    return render(request,"orders/register.html",context)


def register(request):
    if request.method == "POST":
        print("registration")
        form = UserForm(request.POST)
        print(form)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request,new_user)
            return HttpResponseRedirect(reverse("order"))
    else:
        form = UserForm()
    context = {
    "items": Fooditem.objects.all(),
    "cats" : Catergory.objects.all(),
    'form': form
    }
    return render(request, 'orders/register.html',context)



def check_username(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        data = {
        'taken' : User.objects.filter(username__iexact=post_text)
        }
        # if there is data in it means its taken
        return HttpResponse(data['taken'])
