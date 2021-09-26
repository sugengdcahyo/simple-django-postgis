from accounts.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields= ('id','email', 'username', 'last_login', 'is_superuser', 'is_active', 'date_joined')
