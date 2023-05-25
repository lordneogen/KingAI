
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class SER_Cards(serializers.ModelSerializer):
    class Meta:
        model = Cards
        fields = '__all__'

class SER_Num_edu(serializers.ModelSerializer):
    class Meta:
        model = Num_edu
        fields = '__all__'

class SER_Trys(serializers.ModelSerializer):
    class Meta:
        model = Trys
        fields = '__all__'


class SER_Kings(serializers.ModelSerializer):
    class Meta:
        model = Kings
        fields = '__all__'