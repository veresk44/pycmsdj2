from datetime import datetime

from django.shortcuts import render
from django.views.generic.base import View

from .models import Category, Post, Tag


# Create your views here.
class HomeView(View):
    """Home page"""

    def get(self, request):
        category_list = Category.objects.all()
        post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
        return render(request, 'blog/post_list.html', {'categories': category_list, 'post_list': post_list})


class PostDetailView(View):
    def get(self, request, category, slug):
        category_list = Category.objects.all()
        post = Post.objects.get(slug=slug)
        # comments = Comment.objects.filter(post=post)
        return render(request, post.template, {'categories': category_list, 'post': post})


class CategoryView(View):
    """Вывод статей категории"""
    def get(self, request, category_slug):
        category = Category.objects.get(slug=category_slug)
        print(category.id)
        category_posts = Post.objects.filter(category=category.id)
        print(category_posts)
        context = {'category_posts': category_posts, 'category': category}
        return render(request, 'blog/category_detail.html', context)

# class TagView(View):
#     """Вывод статей по тегам"""
#     def get(self, request, tag_slug):
#          tag = Tag.objects.get(slug=tag_slug)
#          post_list = tag.filter()

