from django.test import TestCase
from django.urls import reverse
from .models import Category, Article

class SimpleViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cat = Category.objects.create(category="ТестКат", slug="testkat")
        Article.objects.create(
            title="Тестова стаття", description="Опис", slug="teststat",
            category=cat, main_page=True,
            pub_date="2025-10-20 16:00:00"
        )

    def test_home_status(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_articles_list_url(self):
        url = reverse('articles-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_category_url(self):
        url = reverse('articles-category-list', args=["testkat"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_article_detail_url(self):
        url = reverse('news-detail', kwargs={
            "year": "2025",
            "month": "10",
            "day": "20",
            "slug": "teststat"
        })
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
