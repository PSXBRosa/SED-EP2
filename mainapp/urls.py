from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="home"),
    path('create/', views.create, name="create"),
    path('<slug:slug>/', views.detail, name="detail"),
    path('update/<slug:slug>/', views.update, name="update"),
    path('delete/<slug:slug>/', views.delete, name="delete")

]