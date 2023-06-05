from django.db import DatabaseError
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http.response import JsonResponse
from rest_framework_simplejwt.tokens import AccessToken, TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import UserSerializer, UserDetailsSerializer, UpdateUserDetailsSerializer
from .models import User, UserDetail

errObj = {
  "error": {
    "code": "",
    "message": ""
  }
}
# Create your views here.

def getTokenDetails(bearer_token):
    token = bearer_token.split()[1]
    try:
        access_token = AccessToken(token)
        user_id = access_token['user_id']
        user_is_superuser = access_token['is_superuser']
        return user_id, user_is_superuser
    except TokenError:
        raise TokenError
      
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['is_superuser'] = user.is_superuser
        # ...

        return token
    
class MyTokenObtainPairView(TokenObtainPairView):
      serializer_class = MyTokenObtainPairSerializer


#Signup API would accept the first name, last name, and email phone as input.
@csrf_exempt
@api_view(['POST'])
def signup(request):
    user_data = JSONParser().parse(request)
    users_serializer = UserSerializer(data=user_data)
    try:
        if(users_serializer.is_valid()):
            users_serializer.save()
            return JsonResponse("Signed up Successfully", status=201, safe=False)
    except DatabaseError as e:
        errObj['error']['code'] = "400"
        errObj['error']['message'] = "User already exists"+str(e)
        return JsonResponse(errObj, status=400, safe=False)
    return JsonResponse("Failed to add", status=400, safe=False)


#Add User Details API would accept age, date of birth, profession, address, and hobby for a particular user
@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addUser(request):
    user_details_data = JSONParser().parse(request)
    bearer_token = request.headers.get('Authorization', None)
    if bearer_token:
        try:
            user_id, _ = getTokenDetails(bearer_token)
        except TokenError:
            errObj['error']['code'] = "400"
            errObj['error']['message'] = "Authorization error"
            return JsonResponse(errObj, status=400, safe=False)
    user_details_serializer = UserDetailsSerializer(data=user_details_data, context={'userId': user_id})
    if(user_details_serializer.is_valid()):
        try:
            user_details_serializer.save()
            return JsonResponse("Added User Details Successfully", safe=False)
        except DatabaseError as e:
            errObj['error']['code'] = "400"
            errObj['error']['message'] = "Unable to add details as details for the user already exists"
            return JsonResponse(errObj, status=400, safe=False)
    errors = user_details_serializer.errors
    errObj['error']['code'] = "400"
    errObj['error']['message'] = "Failed to add user details: "+ errors 
    return JsonResponse(errObj, status=400, safe=False)


#Update User Profile API should be able to update any of these values profession, address, and hobby for a particular user with the help of a primary key.
@csrf_exempt
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateUser(request):
    user_details_data = JSONParser().parse(request)
    bearer_token = request.headers.get('Authorization', None)
    if bearer_token:
        try:
            user_id, _ = getTokenDetails(bearer_token)
        except TokenError:
            errObj['error']['code'] = "400"
            errObj['error']['message'] = "Authorization error"
            return JsonResponse("Authorization error", status=400, safe=False)
    try:
        user_details = UserDetail.objects.get(user=user_id)
    except UserDetail.DoesNotExist:
        errObj['error']['code'] = "400"
        errObj['error']['message'] = "Unable to update as details for the user does not exist"
        return JsonResponse(errObj, status=400, safe=False) 
    user_details_serializer = UpdateUserDetailsSerializer(user_details, data=user_details_data)
    if(user_details_serializer.is_valid()):
        try:
            user_details_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        except DatabaseError as e:
            errObj['error']['code'] = "400"
            errObj['error']['message'] = "Failed to update "+str(e)
            return JsonResponse(errObj, status=400, safe=False)
    errors = user_details_serializer.errors
    return JsonResponse("Failed to update "+errors, status=400, safe=False)


#Delete User API should delete the user with the help of the primary key
@csrf_exempt
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deleteUser(request):
        #userIdDict = JSONParser().parse(request)
        bearer_token = request.headers.get('Authorization', None)
        if bearer_token:
            try:
                user_id, _ = getTokenDetails(bearer_token)
            except TokenError:
                errObj['error']['code'] = "400"
                errObj['error']['message'] = "Authorization error"
                return JsonResponse(errObj, status=400, safe=False)
        #code for deleting the any user by only supeuser
        '''if(userIdDict):
            if(user_is_superuser):
                user_id=userIdDict['userId']
            else:
                if(userIdDict['userId'] != user_id):
                    return JsonResponse("Only a superuser can delete other users", safe=False)''' 
        try:     
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            errObj['error']['code'] = "400"
            errObj['error']['message'] = "Unable to delete as user does not exist"
            return JsonResponse("Unable to delete as user does not exist", status=400, safe=False)    
        user.delete()
        return JsonResponse("Deleted Successfully", safe=False)
