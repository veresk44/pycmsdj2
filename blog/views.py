from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Post


# Create your views here.
class HomeView(View):
    """Home page"""

    def get(self, request):
        category_list = Category.objects.all()
        posts = Post.objects.all()
        return render(request, 'blog/home.html', {
                                                    'categories': category_list,
                                                    'posts': posts
                                                }
                      )


class CategoryView(View):
    """Вывод статей категории"""
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {'category': category})
