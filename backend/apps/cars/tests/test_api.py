from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from apps.cars.models import CarModel

UserModel = get_user_model()


class CarApiTestCase(APITestCase):
    def setUp(self):
        self.car1 = CarModel.objects.create(
            brand='Skoda',
            price=3000,
            year=2010,
            body_type='Jeep'
        )
        self.car2 = CarModel.objects.create(
            brand='Audi',
            price=20000,
            year=2019,
            body_type='Sedan'
        )

    def _authenticate(self):
        email = 'admin@gmail.com'
        password = 'Simple123.'
        self.client.post(reverse('users_list_create'), {
            'email': email,
            'password': password,
            'profile': {
                'name': 'Max',
                "surname": "Mad",
                "age": 57
            }
        }, format='json')
        user = UserModel.objects.get(email=email)
        user.is_active = True
        user.save()
        res = self.client.post(reverse('auth_login'), {
            'email': email,
            'password': password
        })
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {res.data["access"]}')

    def test_get_all_cars(self):
        res = self.client.get(reverse('cars_list_create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

        data = res.data
        self.assertEqual(len(data), 2)

        car1 = CarModel.objects.get(pk=self.car1.pk)
        self.assertEqual(car1.brand, 'Skoda')

        car2 = CarModel.objects.get(pk=self.car2.pk)
        self.assertEqual(car2.brand, 'Audi')

        self.assertEqual(CarModel.objects.count(), 2)

    def test_create_car_without_auth(self):
        sample_car = {
            'brand': 'KIA',
            'price': 6000,
            'year': 2008,
            'body_type': 'Jeep'
        }
        count_before = CarModel.objects.count()
        res = self.client.post(reverse('cars_list_create'), sample_car)
        count_after = CarModel.objects.count()
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(count_after, count_before)

    def test_create_car_with_auth(self):
        self._authenticate()
        sample_car = {
            'brand': 'KIA',
            'price': 6000,
            'year': 2008,
            'body_type': 'Jeep'
        }
        count_before = CarModel.objects.count()
        res = self.client.post(reverse('cars_list_create'), sample_car)
        count_after = CarModel.objects.count()
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(count_after, count_before + 1)

