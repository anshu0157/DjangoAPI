from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from .models import Advisor
from .serializers import AdvisorSerializer
from django.contrib.auth.models import User



# Create your views here.
class profiles(APIView):
    def post(self, request):
        serializer = AdvisorSerializer(data=request.data)
        # advisor = Advisor.objects.values('name','photo')
        name=request.data.get('name')
        photo=request.data.get('photo')
        # print(name,photo)
        if serializer.is_valid() and ((name and photo) != ""):
            serializer.save()
            # print('success')
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

   

# #User Register
# class UserRegister(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         name=request.data.get('name')
#         email=request.data.get('email')
#         password=request.data.get('password')
#         print(name,email,password)
#         if serializer.is_valid() :
#             user = serializer.save()
#             print('success')
#             if user:
#                 return Response(status=status.HTTP_200_OK)
#         return Response(status=status.HTTP_400_BAD_REQUEST)

# #User login
# class UserLogin(APIView):
#     def post(self, request):
#         return Response('Hello hi')




