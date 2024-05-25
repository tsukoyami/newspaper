from django.db import IntegrityError
from django.test import TestCase
from .models import RegisteredUser

class RegisteredUserTest(TestCase):
  """Tests for the RegisteredUser model"""

  def test_create_user(self):
    """Tests creating a new RegisteredUser object"""
    user = RegisteredUser.objects.create(
        username="test_user",
        password="secretpassword",
        first_name="John",
        last_name="Doe",
        email="test@example.com",
    )
    self.assertEqual(user.username, "test_user")
    self.assertEqual(user.first_name, "John")
    self.assertEqual(user.last_name, "Doe")
    self.assertEqual(user.email, "test@example.com")

  def test_unique_username(self):
    """Tests that username is unique"""
    user1 = RegisteredUser.objects.create(
        username="unique_user",
        password="secretpassword",
        first_name="John",
        last_name="Doe",
        email="unique1@example.com",
    )
    with self.assertRaises(IntegrityError):
        RegisteredUser.objects.create(
            username="unique_user",  # Duplicate username
            password="anotherpassword",
            first_name="Jane",
            last_name="Smith",
            email="unique2@example.com",
        )

  def test_unique_email(self):
    """Tests that email is unique"""
    user1 = RegisteredUser.objects.create(
        username="unique_email",
        password="secretpassword",
        first_name="John",
        last_name="Doe",
        email="unique@example.com",
    )
    with self.assertRaises(IntegrityError):
        RegisteredUser.objects.create(
            username="another_user",
            password="anotherpassword",
            first_name="Jane",
            last_name="Smith",
            email="unique@example.com",  # Duplicate email
        )
