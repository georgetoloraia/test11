# blog/urls.py
from django.urls import path
from .views import *
urlpatterns = [
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('blogs/', BlogList.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetail.as_view(), name='blog-detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', TokenView.as_view(), name='token'),
]

