from django.contrib import admin
from blog.models import Article as ArticleModel
from blog.models import ArticleComment as ArticleCommentModel
from blog.models import Like as LikeModel


admin.site.register(ArticleModel)
admin.site.register(ArticleCommentModel)
admin.site.register(LikeModel)