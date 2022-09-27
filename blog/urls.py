from django.urls import path
from blog import views

urlpatterns = [
    path("", views.ArticleView.as_view()),
    path("<int:article_id>/", views.ArticleView.as_view()),
    path("comment/", views.CommentView.as_view()),
    path("comment/<int:article_id>/", views.CommentView.as_view()),
    path("like/", views.LikeView.as_view()),
    path("like/<int:like_id>/", views.LikeView.as_view()),
]