from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import User, UserSerializer
from api.models import Product, ProductSerializer



"""
The ContactsView will contain the logic on how to:
 GET, POST, PUT or delete the contacts
"""
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


    
