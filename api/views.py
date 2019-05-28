from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken

from api.models import User, UserSerializer
from api.models import Product, ProductSerializer
from api.models import Profile, ProfileSerializer
from api.models import Address, AddressSerializer
from api.models import Category, CategorySerializer
from api.models import Like, LikeSerializer
from api.models import Notification, NotificationSerializer
from api.models import Talk, TalkSerializer


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
            })


class Logout(APIView):
    
    def get(self, request, format=None):

        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserView(APIView):
    
    def get(self, request, user_id=None):

        if user_id is not None:
            user = User.objects.get(id=user_id)
            serializer = UserSerializer(user, many=False)
            return Response(serializer.data)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)

    def post(self, request):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, user_id):

        user = User.objects.get(id=user_id)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)



class ProductView(APIView):
    
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({"products": serializer.data})

    def post(self, request):
        product = request.data.get('product')

        # Create an article from the above data
        serializer = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(product_saved.title)})

class ProfileView(APIView):
    
    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response({"profiles": serializer.data})

    def post(self, request):
        profile = request.data.get('profile')

        # Create an article from the above data
        serializer = ProfileSerializer(data=profile)
        if serializer.is_valid(raise_exception=True):
            profile_saved = serializer.save()
        return Response({"success": "Profile '{}' created successfully".format(profile_saved.id)})


class AddressView(APIView):
    
    def get(self, request):
        address = Address.objects.all()
        serializer = AddressSerializer(address, many=True)
        return Response({"address": serializer.data})

    def post(self, request):
        address = request.data.get('address')

        # Create an article from the above data
        serializer = AddressSerializer(data=address)
        if serializer.is_valid(raise_exception=True):
            address_saved = serializer.save()
        return Response({"success": "Address '{}' created successfully".format(address_saved.id)})


class CategoryView(APIView):
    
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response({"categories": serializer.data})

    def post(self, request):
        category = request.data.get('category')

        # Create an article from the above data
        serializer = CategorySerializer(data=category)
        if serializer.is_valid(raise_exception=True):
            category_saved = serializer.save()
        return Response({"success": "Category '{}' created successfully".format(category_saved.id)})


class LikeView(APIView):
    
    def get(self, request):
        likes = Like.objects.all()
        serializer = LikeSerializer(likes, many=True)
        return Response({"likes": serializer.data})

    def post(self, request):
        like = request.data.get('like')

        # Create an article from the above data
        serializer = LikeSerializer(data=like)
        if serializer.is_valid(raise_exception=True):
            like_saved = serializer.save()
        return Response({"success": "Like '{}' created successfully".format(like_saved.id)})


class NotificationView(APIView):
    
    def get(self, request):
        notifications = Notification.objects.all()
        serializer = NotificationSerializer(notifications, many=True)
        return Response({"notifications": serializer.data})

    def post(self, request):
        notification = request.data.get('notification')

        # Create an article from the above data
        serializer = NotificationSerializer(data=notification)
        if serializer.is_valid(raise_exception=True):
            notification_saved = serializer.save()
        return Response({"success": "Notification '{}' created successfully".format(notification_saved.id)})


class TalkView(APIView):
    
    def get(self, request):
        talks = Talk.objects.all()
        serializer = TalkSerializer(talks, many=True)
        return Response({"talks": serializer.data})

    def post(self, request):
        talk = request.data.get('talk')

        # Create an article from the above data
        serializer = TalkSerializer(data=talk)
        if serializer.is_valid(raise_exception=True):
            talk_saved = serializer.save()
        return Response({"success": "Talk '{}' created successfully".format(talk_saved.id)})

    
    
