from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serilazier import UserSerialzer,DocSeializer
from .models import User,Document
from django.contrib.auth.hashers import check_password
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        serilazer = UserSerialzer(data=request.data)
        serilazer.is_valid(raise_exception=True)
        serilazer.save()
        return Response({'message':'SUCESS'},status=status.HTTP_201_CREATED)
    
class LoginView(APIView):
    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = User.objects.filter(phone_no=username).first()
        
        if user and check_password(password,user.password):
            refresh_token = RefreshToken.for_user(user)
            access_token = refresh_token.access_token
            
            return Response({'access_token':str(access_token),
                             'refresh_token':str(refresh_token)},status=status.HTTP_200_OK)
        return Response({'message':"Worng Credential"},status=status.HTTP_400_BAD_REQUEST)
    
class SaveDoc(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = DocSeializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'SUCESS'},status=status.HTTP_201_CREATED)