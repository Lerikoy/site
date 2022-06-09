from django.urls import path
from . import views

urlpatterns = [
    path('blog', views.BlogPostListView.as_view()),
    path('blog/featured', views.BlogPostFeaturedView.as_view()),
    path('blog/category', views.BlogPostCategoryView.as_view()),
    path('blog/<slug>', views.BlogPostDetailView.as_view()),
    path('tour', views.PostTourListView.as_view()),
    path('tour/featured', views.PostTourFeaturedView.as_view()),
    path('tour/category', views.PostTourCategoryView.as_view()),
    path('tour/<slug>', views.PostTourDetailView.as_view()),
    path('post_image', views.post_image)
]
