from django.utils.decorators import method_decorator

from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from drf_yasg.utils import swagger_auto_schema

from apps.cars.filter import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarPhotoSerializer, CarSerializer


# дозволяє у документації всім користуватися вказаним методом (прибирає замочок)
@method_decorator(name='get',decorator=swagger_auto_schema(security=[],
                                                           operation_summary='get all cars',
                                                           operation_id='get_all_cars'))
# @method_decorator(name='post', decorator=swagger_auto_schema(security=[]))
class CarListView(ListAPIView):
    """
    get:
        get all cars
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (AllowAny,)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:
        get car
    put:
        update car
    patch:
        partial update car
    delete:
        delete car
    """
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

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
