from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.base import View

from .models import Category, Post, Tag, Comment
from .forms import CommentForm


# Create your views here.
# class HomeView(View):
#     """Home page"""
#     def get(self, request):
#         category_list = Category.objects.all()
#         post_list = Post.objects.filter(published_date__lte=datetime.now(), published=True)
#         return render(request, 'blog/post_list.html', {'categories': category_list, 'post_list': post_list})


class PostListView(View):
    """Вывод статей категории"""

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=datetime.now(), published=True)

    def get(self, request, category_slug=None, tag_slug=None):
        # category_list: object = Category.objects.filter(published=True)

        if category_slug is not None:
            posts = self.get_queryset().filter(category__slug=category_slug, category__published=True)
        elif tag_slug is not None:
            posts = self.get_queryset().filter(tags__slug=tag_slug, tags__published=True)
        else:
            posts = self.get_queryset().filter(published_date__lte=datetime.now(), published=True)

        if posts.exists():
            template = posts.first().get_category_template()
        else:
            template = 'blog/post_list.html'
        context = {'post_list': posts}
        return render(request, template, context)

        # category = Category.objects.get(slug=category_slug)
        # print(category.id)
        # category_posts = Post.objects.filter(category=category.id)
        # print(category_posts)
        # context = {'category_posts': category_posts, 'category': category}
        # return render(request, 'blog/category_detail.html', context)


# class TagView(View):
#     """Вывод статей по тегам"""
#     def get(self, request, slug):
#
#         context = {'post_list': posts}
#         return render(request, posts.first().get_category_template(), context)

# def get(self, request, tag_slug):
#      tag = Tag.objects.get(slug=tag_slug)
#      posts_list = tag.tag.all()
#      print(posts_list)
#      context = {'tag': tag, 'posts_list': posts_list}
#      return render(request, 'blog/tag_detail.html', context)

class PostDetailView(View):
    def get(self, request, **kwargs):
        category_list = Category.objects.filter(published=True)
        post = get_object_or_404(Post, slug=kwargs.get('slug'))
        form = CommentForm()
        # comments = Comment.objects.filter(post=post)
        return render(request, post.template,
                      {'categories': category_list, 'post': post, 'form': form}
                      )

    def post(self, request, **kwargs):
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post = Post.objects.get(slug=kwargs.get('slug'))
            form.author = request.user
            form.save()
        return redirect(request.path)


class CreateCommentView(View):
    def post(self, request, pk):
        print(request.POST)
        form = CommentForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.author = request.user
            form.save()

        # comment = Comment()
        # comment.author=request.user
        # comment.post_id = request.POST.get('post')
        # comment.text = request.POST.get('text')
        # comment.save()
        # Comment.objects.create(
        #     author=request.user,
        #     post_id=request.POST.get('post'),
        #     text=request.POST.get('text')
        # )
        return HttpResponse(status=201)
