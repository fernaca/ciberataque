from django.urls import path
from .views import HomeView, ArticleDetailView, DeletePostView #,PostView, UpdatePostView, 

urlpatterns = [
    path('', HomeView.as_view() , name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="detail"),
    # path('add_post/', PostView.as_view(), name="add_post"),
    # path('article/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('article/<int:pk>/delete/', DeletePostView.as_view(), name="delete_post"),

]
