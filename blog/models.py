from django.db import models


class Article(models.Model):
    user = models.ForeignKey("user.User", verbose_name="작성자", on_delete=models.CASCADE)
    
    title = models.CharField("제목", max_length=35)
    content = models.CharField("내용", max_length=500)
    
    created_at = models.DateTimeField("게시글 등록 일자", auto_now_add=True)
    updated_at = models.DateTimeField("게시글 수정 일자", auto_now=True)
    
    def __str__(self):
        return f"id [ {self.id} ] {self.user.username} 님이 작성한 Article"
    

class ArticleComment(models.Model):
    user = models.ForeignKey("user.User", verbose_name="작성자", on_delete=models.CASCADE)
    article = models.ForeignKey(Article, verbose_name="게시글", on_delete=models.CASCADE)

    comment = models.TextField("댓글", max_length=200)

    created_at = models.DateTimeField("게시글 댓글 생성시간", auto_now_add=True)
    updated_at = models.DateTimeField("게시글 댓글 수정시간", auto_now=True)

    def __str__(self):
        return f"{self.user}님이 작성한 댓글 : {self.comment}"


class Like(models.Model):
    article = models.ForeignKey('Article', verbose_name="게시글", on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'id [ {self.id} ] {self.user.username}가 {self.article.title}글을 좋아합니다.'