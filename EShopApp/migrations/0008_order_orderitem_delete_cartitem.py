# Generated by Django 4.2.2 on 2023-08-20 13:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EShopApp', '0007_cart_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateTimeField(auto_now_add=True)),
                ('complete', models.BooleanField(default=False, null=True)),
                ('transaction_id', models.CharField(max_length=100, null=True)),
                ('e_shop_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EShopApp.eshopuser')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EShopApp.order')),
                ('video_game', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='EShopApp.videogame')),
            ],
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
