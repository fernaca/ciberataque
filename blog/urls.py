from django.urls import path
from .views import HomeView, ArticleDetailView, DeletePostView, AddPostView, UpdatePostView, AddPostBanco, BancoView

urlpatterns = [
    path('', HomeView.as_view() , name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="detail"),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name="delete_post"),
    path('add_banco/', AddPostBanco.as_view(), name="add_banco"),
    path('banco/<str:banco>/', BancoView, name="banco"),



]
