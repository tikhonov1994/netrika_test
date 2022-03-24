from django.test import TestCase
from cities.models import Citizen, City


class CitizenModelTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.citizen = Citizen.objects.create(
            name='Test Name',
            city=City.objects.create(
                name='Test City'
            )
        )

    def test_str_name(self):
        """ Проверка строкового отображения объекта жителя"""
        self.assertEqual(str(self.citizen), 'Test Name')


class CityModelTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.city = City.objects.create(
            name='Test City'
        )

    def test_str_name(self):
        """ Проверка строкового отображения объекта города"""
        self.assertEqual(str(self.city), 'Test City')
