from django.urls import path
from . import views

app_name = 'guide'

urlpatterns = [
    path('create_tour', views.create_tour),
    path('list_tour', views.list_tour),
    path('detail_tour/<int:tour_pk>', views.detail_tour),
    path('list', views.list_guide),
    path('paid/<int:trip_pk>', views.paid),
    path('paidtour', views.paidtour),
    path('paider/<int:trip_pk>', views.paider),
    # path('guidetour/<int:tour_pk>', views.guidetour),
]