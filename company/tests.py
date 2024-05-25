from django.test import TestCase

from .models import Company

class ArticleTest(TestCase):

  def test_create_article(self):
    article = Company.objects.create(name="Test Article", url="This is a test article.")
    self.assertEqual(Company.name, "Test Article")
    self.assertEqual(Company.url, "This is a test article.")

