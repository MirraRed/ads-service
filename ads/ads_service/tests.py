from django.test import TestCase
from pymysql import IntegrityError
from .models import User, Advertisement, Location

class UserModelTest(TestCase):
    def setUp(self):
        # Створення тестових даних перед кожним тестом
        location = Location.objects.create(location_name='Test Location')
        User.objects.create(
            login='testuser',
            email='test@example.com',
            user_password='testpassword',
            location=location
        )

    def test_user_creation(self):
        # Перевірка, чи користувач вдало створений
        user = User.objects.get(login='testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.user_password, 'testpassword')
        self.assertEqual(user.location.location_name, 'Test Location')

class AdModelTest(TestCase):
    def setUp(self):
        # Створення тестових даних перед кожним тестом
        location = Location.objects.create(location_name='Test Location')
        user = User.objects.create(
            login='testuser',
            email='test@example.com',
            user_password='testpassword',
            location=location
        )
        Advertisement.objects.create(
            title='Test Ad',
            ad_text='This is a test advertisement',
            location=location,
            author=user,
            is_public=True
        )

    def test_ad_creation(self):
        # Перевірка, чи оголошення вдало створене
        ad = Advertisement.objects.get(title='Test Ad')
        self.assertEqual(ad.ad_text, 'This is a test advertisement')
        self.assertEqual(ad.location.location_name, 'Test Location')
        self.assertEqual(ad.author.login, 'testuser')
        self.assertTrue(ad.is_public)

class LocationModelTest(TestCase):
    def setUp(self):
        # Створення тестових даних перед кожним тестом
        Location.objects.create(location_name='Test Location')

    def test_location_creation(self):
        # Перевірка, чи локація вдало створена
        location = Location.objects.get(location_name='Test Location')
        self.assertEqual(location.location_name, 'Test Location')

    def test_unique_location_name(self):
        # Спроба створити локацію з тим же ім'ям, що і в setUp
        with self.assertRaises(IntegrityError):
            Location.objects.create(location_name='Test Location')
