from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic import DetailView, ListView
from .models import Article, Category

# 1. HomePageView - головна сторінка
class HomePageView(ListView):
    model = Category
    template_name = 'index.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = Article.objects.filter(main_page=True)[:5]  # топ-5 статей для виводу на головну
        return context

# 2. ArticleList - всі статті
class ArticleList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Article.objects.all()

# 3. ArticleCategoryList - статті певної категорії
class ArticleCategoryList(ListView):
    model = Article
    template_name = 'articles_list.html'
    context_object_name = 'items'

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['slug']).distinct()

# 4. ArticleDetail - детальна сторінка статті
class ArticleDetail(DetailView):
    model = Article
    template_name = 'article_detail.html'
    context_object_name = 'item'

    def get_object(self):
        # Фільтрація по даті і слагу (якщо потрібно)
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        slug = self.kwargs['slug']
        return Article.objects.get(
            pub_date__year=year,
            pub_date__month=month,
            pub_date__day=day,
            slug=slug
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['images'] = context['item'].images.all()
        except:
            context['images'] = []
        return context
