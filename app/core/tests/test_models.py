from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    
    def test_create_user_with_successful(self):
        """Test creating a new user with an email is susccessful"""
        email = "test@londonappdev.com"
        password = "testPass123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        """
         the code below check_password is a helper function and
         it returns true if the password is correct or 
         false if its not correct
        """
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalize(self):
        """Test the eamil for a new user is normalized"""

        email = 'test@LONDONAP.COM'

        # this is not testing the password since we have already done that
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""

        #Anything under the context manager should raise a value error. I
        # f it doesn't happen, then it will fail
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test creating a new superuser """
        user = get_user_model().objects.create_superuser(
            'test@londonappdev.com',
            'test123'
        )

        # The is_superuser comes from the PermissionsMixin Django module
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
