# Generated by Django 4.2.2 on 2023-08-19 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VideoGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('list_image', models.ImageField(upload_to='<django.db.models.fields.CharField>/game_data')),
                ('banner_image', models.ImageField(upload_to='<django.db.models.fields.CharField>/game_data')),
                ('screenshot_1', models.ImageField(upload_to='<django.db.models.fields.CharField>/game_data')),
                ('screenshot_2', models.ImageField(upload_to='<django.db.models.fields.CharField>/game_data')),
                ('screenshot_3', models.ImageField(upload_to='<django.db.models.fields.CharField>/game_data')),
                ('genre', models.CharField(max_length=30)),
                ('platform', models.CharField(max_length=30)),
            ],
        ),
    ]