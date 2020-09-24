from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, authentication_classes
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework.response import Response
# from rest_framework import viewsets
from .serializers import *
from .models import *
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import status


# Create your views here.
@api_view(['POST'])
def apply_guide(request):
    User = get_user_model()
    user = get_object_or_404(User, pk=request.user.pk)
    if user.phone_number:
        user.user_code = 1
        user.save()
        return HttpResponse('가이드 획득')
    return HttpResponse('휴대폰 인증 필요')

@api_view(['POST'])
@authentication_classes((JSONWebTokenAuthentication,))
def create_tour(request):
    user = request.user
    serializer = GuideItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=user)
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_tour(request):
    tours = TripItemModel.objects.all()
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)
# class GuideViewSet(viewsets.ModelViewSet):
#     queryset = TripItemModel.objects.all()
#     serializer_class = GuideItemSerializer
#     def perform_create(self, serializer):
#         serializer.save(user_id=self.request.user.pk)

@api_view(['GET'])
def detail_tour(request, tour_pk):
    tour = TripItemModel.objects.filter(pk=tour_pk)
    serializer = TourDetailSerializer(tour, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def list_guide(request, username):
    User = get_user_model()
    user = User.objects.filter(id=username)
    trips = user.TripItemModel_set.all()
    serializer = GuideSerializer(trips, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def paid(request, trip_pk):
    trip = get_object_or_404(TripItemModel, pk=trip_pk)
    tour, flag = GuideTour.objects.get_or_create(user=request.user.pk, trip_item=trip)
    if flag:
        return HttpResponse('결제되었습니다.')
    else:
        return HttpResponse('이미 결제된 여행입니다.')

@api_view(['GET'])
def paidtour(request):
    User = get_user_model()
    user = get_object_or_404(User, pk=request.user.pk)
    tours = user.TripItemModel_set.all()
    serializer = TourSerializer(tours, many=True)
    return Response(serializer.data)