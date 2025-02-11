from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


# Get the custom user model
CustomUser = get_user_model()


class CustomUserModelTests(TestCase):
    def test_create_user(self):
        """Test creating a new user with all require fields."""
        user = CustomUser.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123',
            phone_number='+1234567890',
            data_of_birth='1990-01-01',
        )

        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.phone_number, '+1234567890')
        self.assertEqual(user.date_of_birth, '1990-01-01')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_verified) # Default value