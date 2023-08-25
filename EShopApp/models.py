from django.contrib.auth.models import User
from django.db import models

class EShopUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class VideoGame (models.Model):
    PLATFORM_CHOICES = [
        ('pc', 'PC'),
        ('playstation', 'Playstation'),
        ('xbox', 'XBOX')
    ]

    GENRES = [
        ('action', 'Action'),
        ('adventure', 'Adventure'),
        ('racing', 'Racing'),
        ('horror', 'Horror')
    ]

    title = models.CharField(max_length=30)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=4)
    list_image = models.ImageField(upload_to="images/")
    banner_image = models.ImageField(upload_to="images/")
    screenshot_1 = models.ImageField(upload_to="images/")
    screenshot_2 = models.ImageField(upload_to="images/")
    screenshot_3 = models.ImageField(upload_to="images/")
    genre = models.CharField(max_length=20, choices=GENRES, default="PC")
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES, default="PC")


class Order(models.Model):
    e_shop_user = models.ForeignKey(EShopUser, on_delete=models.SET_NULL, null=True, blank=True)
    complete = models.BooleanField(default=False, null=True, blank=False)

    @property
    def get_cart_total(self):
        order_items = self.orderitem_set.all()
        total = sum([item.video_game.price for item in order_items])
        return total

    @property
    def get_cart_items(self):
        order_items = self.orderitem_set.all()
        total = len(order_items)
        return total

class OrderItem(models.Model):
    video_game = models.ForeignKey(VideoGame, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)


# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     address = models.CharField(max_length=200, null=False)
#     city = models.CharField(max_length=200, null=False)
#     state = models.CharField(max_length=200, null=False)
#     zipcode = models.CharField(max_length=200, null=False)
#     date_added = models.DateTimeField(auto_now_add=True)

