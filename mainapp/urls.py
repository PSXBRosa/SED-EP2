from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexListView.as_view(), name="home"),
    path('create/', views.PostCreateView.as_view(), name="create"),
    path('search/', views.search, name='search'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name="detail"),
    path('update/<slug:slug>/', views.PostUpdateView.as_view(), name="update"),
    path('delete/<slug:slug>/', views.PostDeleteView.as_view(), name="delete"),
    path('comment/<int:post_id>/', views.create_comment, name='comment'),
]