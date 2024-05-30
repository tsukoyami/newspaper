from django.db import IntegrityError
from django.test import TestCase
from .models import Source
from registereduser.models import RegisteredUser

# Create your tests here.
class SourceTest(TestCase):
  """Tests for the Source model"""

  def test_create_source(self):
    """Tests creating a new Source object"""
    user = RegisteredUser.objects.create(
        username="test_user",
        password="secretpassword",
        first_name="John",
        last_name="Doe",
        email="test@example.com",
    )
    source = Source.objects.create(
        source_user=user,
        source_name="Test Source",
        source_url="https://www.example.com/source",
    )
    self.assertEqual(source.source_name, "Test Source")
    self.assertEqual(source.source_url, "https://www.example.com/source")

  def test_unique_source_per_user(self):
    """Tests that a user cannot have duplicate sources with the same URL"""
    user = RegisteredUser.objects.create(
        username="test_user",
        password="secretpassword",
        first_name="John",
        last_name="Doe",
        email="test@example.com",
    )
    source1 = Source.objects.create(
        source_user=user,
        source_name="Test Source",
        source_url="https://www.example.com/source",
    )
    with self.assertRaises(IntegrityError):
        Source.objects.create(
            source_user=user,
            source_name="Another Source",
            source_url="https://www.example.com/source",  # Duplicate URL for user
        )
