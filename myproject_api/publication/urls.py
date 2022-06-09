from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogPostListView.as_view()),
    path('featured', views.BlogPostFeaturedView.as_view()),
    path('category', views.BlogPostCategoryView.as_view()),
    path('<slug>', views.BlogPostDetailView.as_view()),
    path('post_image', views.post_image)
]
