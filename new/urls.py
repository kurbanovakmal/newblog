from django.urls import path
from .views import BlogPostViews

urlpatterns = [
    path('',BlogPostViews.as_view(),name='home')
]