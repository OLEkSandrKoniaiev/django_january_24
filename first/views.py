from rest_framework.response import Response
from rest_framework import status
from django.forms import model_to_dict
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.db.models import Q

from first.models import CarModel
from first.serializers import CarSerializer
from first.filter import car_filter

from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    CreateModelMixin


# class CarListCreateView(GenericAPIView):
#     def get(self, *args, **kwargs):
#         # qs = CarModel.objects.all()  # qs - query set
#         # qs = qs.filter(brand__in=['bmw', 'mers'], year=2004)  # наче sql запити
#
#         # Виконує логічне і при фільтрації
#         # qs = CarModel.objects.filter(brand__in=['bmw', 'mers'], year=2004)  # можна одразу фільтрувати
#
#         # Для або необхідно імпортувати Q
#         # qs = qs.filter(Q(brand__in=['bmw', 'mers']) | Q(year=2004))
#
#         # Проте до Q можна також використовувати логічне і
#         # qs = qs.filter(Q(brand__in=['bmw', 'mers']) | Q(year=2004) & Q(price=2000))
#
#         # Також можна робити виключення, сортування тощо:
#         # qs = qs.filter(Q(brand__in=['bmw', 'mers']) | Q(year=2004)).exclude(brand='bmw')
#
#         # qs = qs.filter(Q(brand__in=['bmw', 'mers']) | Q(year=2004)).exclude(brand='bmw').count()
#         # print(qs)
#
#         # qs = qs.filter(Q(brand__in=['bmw', 'mers']) | Q(year=2004) & Q(price=2000)).order_by('price')
#         # qs = qs.filter(Q(brand__in=['bmw', 'mers']) | Q(year=2004) & Q(price=2000)).order_by('-price')  # для звороту
#         # qs = qs.filter(Q(brand__in=['bmw', 'mers']) | Q(year=2004) & Q(price=2000)).order_by('price', 'brand')
#
#         # qs = qs.filter(Q(brand__in=['bmw', 'mers']) | Q(year=2004) & Q(price=2000)).order_by('price', 'brand').reverse()
#
#         # qs = qs.filter(Q(brand__in=['bmw', 'mers']) | Q(year=2004)).values('id', 'brand')
#         # print(qs.query)  # щоб переглянути "sql" запит
#
#         # qs = CarModel.objects.all()[:2]  # можна застосовувати зрізи
#         # qs = CarModel.objects.all()[2:4:2]  # кроки краще не задавати
#
#         qs = CarModel.objects.all()
#
#         serializer = CarSerializer(qs, many=True)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def post(self, *args, **kwargs):
#         data = self.request.data
#         serializer = CarSerializer(data=data)
#         # if not serializer.is_valid():
#         #     return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_201_CREATED)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     def get(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found", status.HTTP_404_NOT_FOUND)
#         car = self.get_object()  # сам витягує pk перевіряє чи є такий pk у базі і повертає car
#         serializer = CarSerializer(car)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found", status.HTTP_404_NOT_FOUND)
#         data = self.request.data
#         car = self.get_object()
#         serializer = CarSerializer(car, data=data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def patch(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         # except CarModel.DoesNotExist:
#         #     return Response("not found", status.HTTP_404_NOT_FOUND)
#         car = self.get_object()
#         data = self.request.data
#         serializer = CarSerializer(car, data=data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def delete(self, *args, **kwargs):
#         # pk = kwargs['pk']
#         # try:
#         #     car = CarModel.objects.get(pk=pk)
#         #     car.delete()
#         # except CarModel.DoesNotExist:
#         #     return Response("not found", status.HTTP_404_NOT_FOUND)
#         self.get_object().delete()
#         return Response(status.HTTP_204_NO_CONTENT)


############################################################################

# class CarListCreateView(GenericAPIView, CreateModelMixin, ListModelMixin):
#     serializer_class = CarSerializer
#     # queryset = CarModel.objects.all()
#
#     def get_queryset(self):
#         return car_filter(self.request.query_params)
#
#     def post(self, request, *args, **kwargs):
#         return super().create(request, *args, **kwargs)
#
#     # Також ми можемо впливати на серіалайзер та ґет обджект перевизначаючи їх
#     # def get_serializer(self, *args, **kwargs):
#     #     return super().get_serializer(*args, **kwargs)
#     #
#     # def get_object(self):
#     #     return super().get_object()
#
#     # Якщо необхідно щось зробити перед збереженням до дб
#     def perform_create(self, serializer):
#         super().perform_create(serializer)
#
#     def get(self, request, *args, **kwargs):
#         return super().list(request, *args, **kwargs)
#
#
# class CarRetrieveUpdateDestroyView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     serializer_class = CarSerializer
#     queryset = CarModel.objects.all()
#
#     # Якщо необхідно щось зробити перед оновленням до дб
#     def perform_update(self, serializer):
#         super().perform_update(serializer)
#
#     # Якщо необхідно щось зробити перед видаленням
#     def perform_destroy(self, instance):
#         super().perform_destroy(instance)
#
#     def get(self, request, *args, **kwargs):
#         return super().retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return super().update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         return super().partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return super().destroy(request, *args, **kwargs)

############################################################################

class CarListCreateView(ListCreateAPIView):
    serializer_class = CarSerializer

    def get_queryset(self):
        return car_filter(self.request.query_params)


class CarRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
