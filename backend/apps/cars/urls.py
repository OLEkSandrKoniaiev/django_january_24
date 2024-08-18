from django.urls import path

from apps.cars.views import CarAddPhotoView, CarListView, CarRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListView.as_view(), name='cars'),
    path('/<int:pk>', CarRetrieveUpdateDestroyView.as_view(), name='car'),
    path('/<int:pk>/photo', CarAddPhotoView.as_view(), name='car_photo'),
    # path('/test', TestEmailView.as_view()),
]
