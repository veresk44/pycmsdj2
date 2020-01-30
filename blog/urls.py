import path as path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    # path('comment/<int:pk>/', views.CreateCommentView.as_view(), name='add-comment'),
    path('tag/<slug:tag_slug>/', views.PostListView.as_view(), name='tag'),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name='detail_post'),
    path('<slug:category_slug>/', views.PostListView.as_view(), name='category'),
    path('', views.PostListView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


