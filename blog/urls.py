import path as path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('tag/<slug:tag_slug>/', views.TagView.as_view(), name='tag'),
    path('<slug:category>/<slug:slug>/', views.PostDetailView.as_view(), name='detail_post'),
    path('<slug:category_slug>/', views.CategoryView.as_view(), name='category'),
    path('', views.HomeView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


