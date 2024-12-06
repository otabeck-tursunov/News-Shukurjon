from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import *


class HomeView(View):
    def get(self, request):
        top9_articles = Article.objects.filter(published=True).order_by('-views')[:9]
        context = {
            'top4_articles': top9_articles[:4],
            'top9_articles': top9_articles,
        }
        return render(request, 'index.html', context)

    def post(self, request):
        email = request.POST.get('email')
        if email is not None:
            Newsletter.objects.create(email=email)
        return redirect('home')


class ArticleDetailsView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        same_articles = Article.objects.filter(category=article.category).order_by('-created_at')[:5]
        context = {
            'article': article,
            'same_articles': same_articles,
        }
        return render(request, 'detail-page.html', context)

    def post(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        Comment.objects.create(
            author=request.POST.get('author'),
            email=request.POST.get('email'),
            text=request.POST.get('text'),
            article=article,
        )
        return redirect('article-details', slug=slug)