import django.contrib.auth
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from EShopApp.decorators import allowed_users, unauthenticated_user
from EShopApp.forms import VideoGameForm, CreateUserForm
from EShopApp.models import *


# Create your views here.
def home_page(request):
    return render(request, "homePage.html")


def game_list(request):
    games = VideoGame.objects.all()
    genre = request.GET.get('genre')
    if genre is not None:
        games = VideoGame.objects.filter(genre=genre).all()

    platform = request.GET.get('platform')
    if platform is not None:
        games = VideoGame.objects.filter(platform=platform).all()

    search = request.GET.get('search')
    if search is not None:
        games = VideoGame.objects.filter(title__icontains=search).all()
    page = Paginator(games, 4)
    page_number = request.GET.get('page')
    page = page.get_page(page_number)

    return render(request, "gameList.html", context={"games": games, 'page': page})


@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin'])
def add_game(request):
    if request.method == "POST":
        form = VideoGameForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            game = form.save(commit=False)
            game.save()
            return redirect("game_list")
    return render(request, "addGame.html", context={"form": VideoGameForm})


def details(request, game_id=0):
    video_game = VideoGame.objects.get(pk=game_id)
    return render(request, "details.html", context={"videoGame": video_game})


@login_required(login_url='loginPage')
@allowed_users(allowed_roles=['e_shop_user', 'admin'])
def shopping_cart(request):
    total_price = 0
    total_items = 0
    if request.user.is_authenticated:
        current_user = EShopUser.objects.get(user=request.user)
        order, created = Order.objects.get_or_create(e_shop_user=current_user, complete=False)
        items = order.orderitem_set.all()
        total_price = order.get_cart_total
        total_items = order.get_cart_items
    else:
        items = []
    context = {'items': items, 'total_items': total_items, 'total_price': total_price}
    return render(request, 'shoppingCart.html', context)


@unauthenticated_user
def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home_page')
        else:
            messages.add_message(request, messages.ERROR, 'Invalid Credentials!')

    return render(request, "login.html")


@unauthenticated_user
def register_page(request):
    form = CreateUserForm()
    e_shop_user = EShopUser()
    errors = ''
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='e_shop_user')
            user.groups.add(group)
            e_shop_user.user = user
            e_shop_user.username = user.username
            e_shop_user.email = user.email
            e_shop_user.save()
            return redirect('login_page')
        else:
            errors = form.errors

    context = {"form": form, "errors": errors}
    return render(request, "register.html", context=context)


@login_required(login_url='login')
def logout(request):
    django.contrib.auth.logout(request)
    return redirect('home_page')


@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin', 'e_shop_user'])
def add_to_cart(request, video_game_id):
    video_game = VideoGame.objects.filter(id=video_game_id).first()
    current_user = EShopUser.objects.get(user=request.user)
    order, created = Order.objects.get_or_create(e_shop_user=current_user, complete=False)
    if order is None:
        order = created
    order_item = order.orderitem_set.filter(video_game=video_game).first()
    if order_item:
        pass
    else:
        order_item = OrderItem()
        order_item.video_game = video_game
        order_item.order = order
    order_item.save()

    return redirect('game_list')


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin', 'e_shop_user'])
def remove_from_cart(request, order_item_id):
    current_user = EShopUser.objects.get(user=request.user)
    order, created = Order.objects.get_or_create(e_shop_user=current_user, complete=False)
    if order is None:
        order = created
    order_item = order.orderitem_set.filter(id=order_item_id).first()
    if order_item:
        order_item.delete()
    return redirect('shopping_cart')


@login_required(login_url='login_page')
@allowed_users(allowed_roles=['admin', 'e_shop_user'])
def checkout(request):
    current_user = EShopUser.objects.get(user=request.user)
    order = current_user.order_set.get(complete=False)
    order.complete = True
    order.save()
    return render(request, "checkout.html")
