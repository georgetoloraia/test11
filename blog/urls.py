from django.urls import path
from .views import *

urlpatterns = [
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/', BlogCreateView.as_view(), name='blog-create'),
    path('blogs/<int:id>/', BlogDetailView.as_view(), name='blog-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('token/', TokenGenerationView.as_view(), name='token-generation'),
    path('login/', LoginView.as_view(), name='login'),
]
