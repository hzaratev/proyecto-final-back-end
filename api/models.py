"""
All your application modules and serializers are going to be declared inside this file
"""
from rest_framework import serializers
from django.db import models

"""
Define he Contact Entity into your applcation model
"""
class Contact(models.Model):
    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    phone_number = models.CharField(max_length=15, default='')
    email = models.CharField(max_length=150, default='')

"""
The ContactSerializer is where you will specify what properties
from the ever Contact should be inscuded in the JSON response
"""
class ContactSerializer(serializers.ModelSerializer):


    class Meta:
        model = Contact
        # what fields to include?
        fields = ('first_name','last_name', 'phone_number', 'email')

class User(models.Model):
    user_name = models.CharField(max_length=50, default='')
    email = models.CharField(max_length=150, default='')
    password = models.CharField(max_length=50, default='')


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ('id', 'user_name','email', 'password')


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
    contact_title = models.CharField(max_length=50, default='')
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
    parent = models.ForeignKey('self', on_delete=models.DO_NOTHING, null=True, related_name='categoria')


class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ('category_name', 'state', 'parent')


class Product(models.Model):
    product_name = models.CharField(max_length=50, default='')
    photo = models.CharField(max_length=150, default='')
    description = models.CharField(max_length=500, default='')
    quantity = models.IntegerField()
    date_upload = models.DateField()
    user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    category_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)


class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = ('product_name', 'photo', 'description', 'quantity', 'date_upload', 'user_id', 'category_id', 'address_id')


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
        fields = ('message', 'usr_from', 'user_to')
