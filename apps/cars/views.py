from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from apps.cars.filter import CarFilter
from apps.cars.models import CarModel
from apps.cars.serializers import CarSerializer


class CarListView(ListAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filterset_class = CarFilter
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        print(self.request.user.profile.name, '!!!!!!!!!!!!!!!')
        return super().get_queryset()


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()

    # permission_classes = (IsAuthenticated,)  #працюватиме на всі методи
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return (IsAuthenticated(),)
        return (AllowAny(),)
