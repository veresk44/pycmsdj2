from django.urls import path

from . import views

urlpatterns = [
    path('category/<slug:category_name>/', views.CategoryView.as_view(), name='category'),
    path('', views.HomeView.as_view())
]

