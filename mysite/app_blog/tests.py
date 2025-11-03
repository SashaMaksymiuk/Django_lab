from django.test import TestCase
from django.urls import reverse
from .models import Category, Article

class SimpleTests(TestCase):

    def setUp(self):
        cat = Category.objects.create(category="ТестКат", slug="testkat")
        Article.objects.create(
            title="Тестова стаття", description="Опис", slug="teststat",
            category=cat, main_page=True
        )

    def test_home_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_url(self):
        url = reverse('articles-category-list', args=["testkat"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_absolute_url_category(self):
        cat = Category.objects.get(slug="testkat")
        self.assertEqual(cat.get_absolute_url(), reverse('articles-category-list', args=["testkat"]))
