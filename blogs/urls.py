from django.contrib import admin
from django.urls import path
from blogs.views import (blog_view, 
    BlogAPIView, 
    BlogListCreateAPIView,
    BlogRetrtieveUpdateDestroyAPIView,
    BlogViewSets,
    BlogModelViewSets)

blog_list = BlogViewSets.as_view({
    'get': 'list'
})

blog_detail = BlogViewSets.as_view({
    'get': 'retrieve',
})

blog_list_modelvs = BlogModelViewSets.as_view({
    'get': 'list',
})

blog_detail_modelvs = BlogModelViewSets.as_view({
    'get': 'retrieve'
})
urlpatterns = [
    path('cbv/', blog_view),
    #blogs/apiviews/
    path('apiviews/', BlogAPIView.as_view()),
    path('generics/', BlogListCreateAPIView.as_view()),
    path('generics/<int:pk>/', BlogRetrtieveUpdateDestroyAPIView.as_view()),
    path('viewsets/', blog_list, name='blog-list'),
    path('viewsets/<int:pk>/', blog_detail, name='blog-detail'),
    path('model_viewsets/', blog_list_modelvs),
    path('model_viewsets/<int:pk>/', blog_detail_modelvs)
]