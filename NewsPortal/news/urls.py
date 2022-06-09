from django.urls import path
from .views import PostList, PostDetail, PostSearch, PostUpdateView, PostDeleteView, PostCreate, ArticleList

urlpatterns = [
    path('', PostList.as_view()),
    path('article/', ArticleList.as_view(), name='article_list'),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', PostSearch.as_view(), name='search'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='edit'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('create/', PostCreate.as_view(), name='post_create'),

]