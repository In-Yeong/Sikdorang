from rest_framework.serializers import ReadOnlyField
from rest_framework import serializers
from accounts.serializers import UserSerializer

from .models import *

class GuideItemSerializer(serializers.ModelSerializer):
    guide_user = ReadOnlyField(source='user.id')
    class Meta: 
        model = TripItemModel
        fields = ['guide_user', 'title_img', 'title', 'area', 'start_date', 'end_date', 'price', 'start_point', 'start_time', 'content']

class GuideSerializer(serializers.ModelSerializer):
    
    class Meta: 
        model = TripItemModel
        depth = 1
        fields = ['id', 'user', 'title_img', 'title', 'area', 'start_date', 'end_date', 'price', 'start_point', 'start_time']

class TourSerializer(serializers.ModelSerializer):
    class Meta: 
        model = TripItemModel
        fields = ['id', 'title_img', 'title', 'area', 'start_date', 'end_date', 'price']