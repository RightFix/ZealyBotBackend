from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CreateUserSerializer
from .models import User
from django.shortcuts import get_object_or_404
# Create your views here.

class CreateUser(APIView):
    def post(self, request):
        serializer = CreateUserSerializer(data= request.data)
        try:
            if serializer.is_valid():
                User.objects.create(user_id = request.data['user_id'])
                return Response({"success": True, "message": "User Created Succesfully"})
            else:
                return Response({"success": False, "message": "User Not Created Succesfully"})
        
        except Exception as error:
            return Response({"success": False, "message": f"Error {error}"})    
        

    def get(self,request, pk):
        user = get_object_or_404(User, user_id = pk)
        try:
            if user:
                serializer = CreateUserSerializer(user)
                return Response({"success": True, "message": serializer.data})
            
            else:
                return Response({"success": True, "message": user})
                
            
        except Exception as error:
            return Response({"succes": False, "message": f"Error {error}"}) 

class Community(APIView):
    def patch(request):
        pass

    def get(request):
        pass



    