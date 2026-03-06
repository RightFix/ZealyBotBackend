from rest_framework import serializers
from .models import User
class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'created_at', 'updated_at', 'community']
        read_only_fields= ['created_at', 'updated_at']         

    