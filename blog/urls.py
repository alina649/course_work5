from django.urls import path
from django.views.decorators.cache import cache_page

from . import views
from blog.apps import BlogConfig
from .views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDelete, HomeIndex

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list/', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('edit/<int:pk>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<int:pk>/', BlogDelete.as_view(), name='delete'),
    path('home/', cache_page(60)(HomeIndex), name='home_index'),

]