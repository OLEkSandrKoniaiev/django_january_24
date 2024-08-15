from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from core.permissions.is_admin_or_write_only import IsAdminOrWriteOnly

from apps.cars.filter import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny,)

    # def get_queryset(self):
    #     print(self.request.user.profile.name, '!!!!!!!!!!!!!!!')
    #     return super().get_queryset()


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    # permission_classes = (IsAuthenticated,)  #працюватиме на всі методи
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthenticated(),)
        return (AllowAny(),)


class CarAddPhotoView(UpdateAPIView):
    serializer_class = CarPhotoSerializer
    queryset = CarModel.objects.all()
    permission_classes = (AllowAny,)

    http_method_names = ('put',)

    def perform_update(self, serializer):
        car = self.get_object()
        car.photo.delete()
        super().perform_update(serializer)


