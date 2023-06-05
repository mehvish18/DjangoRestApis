from rest_framework import serializers
from .models import User, UserDetail

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number','password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['email'], validated_data['first_name'], validated_data['last_name'], validated_data['phone_number'], validated_data['password'])
        return user
    
class UserDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model= UserDetail
        fields = ('age', 'dob', 'profession', 'address', 'hobby')

    def create(self, validated_data):
        userId = self.context['userId']
        userDetail = UserDetail()
        userDetail.age = validated_data['age']
        userDetail.dob = validated_data['dob']
        userDetail.profession = validated_data['profession']
        userDetail.address = validated_data['address']
        userDetail.hobby = validated_data['hobby']
        userDetail.user_id = userId
        userDetail.save()
        return userDetail
    

class UpdateUserDetailsSerializer(serializers.ModelSerializer):
    age = serializers.IntegerField(required=False)
    dob = serializers.DateField(required=False)
    profession = serializers.CharField(max_length=150, required=False)
    address = serializers.CharField(max_length=500, required=False)
    hobby = serializers.CharField(max_length=150, required=False)
    class Meta:
        model= UserDetail
        fields = ('age', 'dob', 'profession', 'address', 'hobby')

    def create(self, validated_data):
        userId = self.context['userId']
        userDetail = UserDetail()
        userDetail.age = validated_data['age']
        userDetail.dob = validated_data['dob']
        userDetail.profession = validated_data['profession']
        userDetail.address = validated_data['address']
        userDetail.hobby = validated_data['hobby']
        userDetail.user_id = userId
        userDetail.save()
        return userDetail
    

