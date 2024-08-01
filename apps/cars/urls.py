from django.urls import path

from apps.cars.views import CarListCreateView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='cars'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='car'),
]