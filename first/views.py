from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.forms import model_to_dict

from first.models import CarModel


# class CarListCreateView(APIView):
#     def get(self, *args, **kwargs):
#         print(self.request.query_params.dict())  # request містить в собі всю інформацію яка надходить від клієнта
#         # за допомогою request.query_params.dict() - queri параметрів також можна дістати pk
#         return Response("Hello World get all")
#
#     def post(self, *args, **kwargs):
#         print(self.request.data)  # основний спосіб передачі даних між клієнтом та сервером
#         return Response("Hello World post")
#
#
#
# class CarRetrieveUpdateDestroyView(APIView):
#     def get(self, *args, **kwargs):
#         # print(kwargs['pk'])  # спосіб витягнути pk
#         return Response("Hello World get single")
#
#     def put(self, *args, **kwargs):
#         return Response("Hello World put")
#
#     def patch(self, *args, **kwargs):
#         return Response("Hello World patch")
#
#     def delete(self, *args, **kwargs):
#         return Response("Hello World delete")


# CRUD операції
# C - create
# R - read/retrieve
# U - update
# D - delete/destroy

class CarListCreateView(APIView):
    def get(self, *args, **kwargs):
        cars = CarModel.objects.all()
        res = [model_to_dict(car) for car in cars]
        return Response(res, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        car = CarModel.objects.create(**data)
        car_dict = model_to_dict(car)
        return Response(car_dict, status.HTTP_201_CREATED)


class CarRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs['pk']  # kwargs.get('pk')
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response("not found", status.HTTP_404_NOT_FOUND)
        res = model_to_dict(car)
        return Response(res, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs['pk']
        data = self.request.data
        try:
            car = CarModel.objects.get(pk=pk)
        except CarModel.DoesNotExist:
            return Response("not found", status.HTTP_404_NOT_FOUND)
        car.brand = data['brand']
        car.price = data['price']
        car.year = data['year']
        car.save()
        res = model_to_dict(car)
        return Response(res, status.HTTP_200_OK)

    # def patch(self, *args, **kwargs):
    #     return Response("Hello World patch")

    def delete(self, *args, **kwargs):
        pk = kwargs['pk']
        try:
            car = CarModel.objects.get(pk=pk)
            car.delete()
        except CarModel.DoesNotExist:
            return Response("not found", status.HTTP_404_NOT_FOUND)
        return Response(status.HTTP_204_NO_CONTENT)
