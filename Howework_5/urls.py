"""
URL configuration for Howework_5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from EShopApp.views import home_page, game_list, details, shopping_cart, login_page, register_page, checkout, add_game, \
    logout, add_to_cart, remove_from_cart

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page, name="home_page"),
    path('add/', add_game, name="add_game"),
    path('games/', game_list, name="game_list"),
    path('details/<int:game_id>', details, name="details"),
    path('cart/', shopping_cart, name="shopping_cart"),
    path('login/', login_page, name="login_page"),
    path('register/', register_page, name="register_page"),
    path('checkout/', checkout, name="checkout"),
    path('logout/', logout, name="logout"),
    path('add-to-cart/<int:video_game_id>', add_to_cart, name="add_to_cart"),
    path('remove/<int:order_item_id>', remove_from_cart, name='remove_from_cart'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
