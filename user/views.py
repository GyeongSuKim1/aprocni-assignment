from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import User as UserModel

from user.serializers import UserSerializer


class UserView(APIView):
    authentication_classes = [JWTAuthentication]
    def get(self,request):
        all_users = UserModel.objects.all()        
        return Response(UserSerializer(all_users, many=True).data)

    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)