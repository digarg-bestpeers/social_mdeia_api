from django.urls import path
from network.api import views

urlpatterns = [
    path('list/', views.PostList.as_view()),
    path('create/', views.PostCreate.as_view()),
    path('delete/<int:pk>/', views.PostDestroy.as_view()),
    path('edit/<int:pk>/', views.PostUpdate.as_view()),
    path('posts/', views.AllPostList.as_view()),
    path('search/', views.SearchPost.as_view()),
    path('like/', views.LikePost.as_view()),

]
