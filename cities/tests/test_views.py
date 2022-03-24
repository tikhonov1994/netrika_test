from django.test import Client, TestCase
from django.urls import reverse

from cities.models import Citizen, City


class CitizenViewTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.client = Client()
        cls.citizen = Citizen.objects.create(
            name='Test Name',
            city=City.objects.create(
                name='Test City'
            )
        )

    def test_show_correct_context(self):
        response = self.client.get(
            reverse('cities:city', kwargs={'city': 'Test City'})
        )
        self.assertEqual(response.context.get('page_obj')[0].name,
                         'Test Name')
        self.assertEqual(response.context.get('city'),
                         'Test City')


class CityViewTests(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.client = Client()
        cls.city = City.objects.create(
            name='Test City'
        )
        cls.citizen = Citizen.objects.create(
            name='Test Name',
            city=cls.city
        )

    def test_show_correct_context(self):
        response = self.client.get(
            reverse('cities:index')
        )
        self.assertEqual(response.context.get('page_obj')[0].name,
                         'Test Name')
        self.assertEqual(response.context.get('top_cities')[0].name,
                         'Test City')
