from django.shortcuts import render
from django.contrib.auth import login
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer, RegisterSerializer,BookCallSerializer
from rest_framework.views import APIView
from rest_framework import generics, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import BookAdvisor
#import for Advisor
from network_API.models import Advisor
from network_API.serializers import AdvisorSerializer

# Create your views here.



class UserRegister(APIView):
    def getuserid(self,uid):
        s=uid
        return s
    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')
        # print(userid,username,email,password)
        if serializer.is_valid(raise_exception=True) and ((username and email and password) != ""):
            user=serializer.save()
            # p=self.getuserid(user.id)
            refresh = RefreshToken.for_user(user)
            return Response({'user_id':user.id,'refresh': str(refresh), 'access': str(refresh.access_token)},status=status.HTTP_200_OK)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)
 
 #User login
class UserLogin(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        # print(data)
        email=request.data.get('email')
        password=request.data.get('password')
        if serializer.is_valid(raise_exception=True) and ((email and password) != ""):
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            login(request, user)
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserAdvisor(APIView):
    def get(self, request,uid):
        advisor = Advisor.objects.all()
        # print(advisor.values('name','id'))
        serializer = AdvisorSerializer(advisor, many=True)
        return Response({'advisor_data':advisor.values('name','photo','id')})
    
    def post(self,request,uid,Aid):
        serializer=BookCallSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

class BookedCalls(APIView):
    def get(self,request,uid):
        BookedTime=BookAdvisor.objects.all()
        advisor = Advisor.objects.all()
        # print(advisor.values('name','id'))
        serializer = AdvisorSerializer(advisor, many=True)
        return Response({'advisor_data':[advisor.values('name','photo','id'),BookedTime.values('id','BookingTime')]})

