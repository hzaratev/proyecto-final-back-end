"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=150, default='')
    password = models.CharField(max_length=50, default='')


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id', 'user_name', 'email', 'password')


class Profile(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=50, default='')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class ProfileSerializer(serializers.ModelSerializer):


    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'phone_number', 'user_id')


class Address(models.Model):
    contact_title = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default='')
    city = models.CharField(max_length=50, default='')
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class AddressSerializer(serializers.ModelSerializer):


    class Meta:
        model = Address
        fields = ('contact_title', 'address', 'city', 'user_id')



class Category(models.Model):
    category_name = models.CharField(max_length=50, default='')
    state = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, blank=True, null=True, related_name='categoria')


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ('category_name', 'state', 'parent')


class Product(models.Model):
    title = models.CharField(max_length=50, null=True)
    description = models.CharField(max_length=500, default='')
    image = models.TextField(default='')
    quantity = models.IntegerField()
    pub_date = models.DateField('date published', null=True)
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)


class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'quantity', 'pub_date', 'user_id', 'category_id')


class Like(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    product_id = models.ForeignKey(Product, on_delete=models.DO_NOTHING)


class LikeSerializer(serializers.ModelSerializer):


    class Meta:
        model = Like
        fields = ('')

class Notification(models.Model):
    description = models.CharField(max_length=50, default='')
    state = models.CharField(max_length=50, default='')

class NotificationSerializer(serializers.ModelSerializer):


    class Meta:
        model = Notification
        fields = ('description', 'state')


class Talk(models.Model):
    message = models.CharField(max_length=250, default='')
    usr_from = models.ForeignKey(User, related_name='usr_from', on_delete=models.DO_NOTHING)
    usr_to = models.ForeignKey(User, related_name='usr_to', on_delete=models.DO_NOTHING)


class TalkSerializer(serializers.ModelSerializer):


    class Meta:
        model = Talk
        fields = ('message', 'usr_from', 'usr_to')