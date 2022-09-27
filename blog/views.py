from functools import partial
from os import stat
from django.shortcuts import render
from django.db.models.query_utils import Q

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from blog.serializers import ArticleSerializer
from blog.serializers import CommentSerializer
from blog.serializers import LikeSerializer

from blog.models import Article as ArticleModel
from blog.models import ArticleComment as ArticleCommentModel
from blog.models import Like as LikeModel

from rest_framework_simplejwt.authentication import JWTAuthentication


authentication_classes = [JWTAuthentication]

class ArticleView(APIView):
    def get(self, request):
        articles = ArticleModel.objects.all().order_by('-created_at')
        serialized_data = ArticleSerializer(articles, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)
   
    def post(self, request):
        data = request.data
        data["user"] = request.user.id
        article_serializer = ArticleSerializer(data=data)

        if article_serializer.is_valid():
            article_serializer.save()
            return Response({"message": "게시글이 작성 되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, article_id):
        article = ArticleModel.objects.get(id=article_id)
        article_serializer = ArticleSerializer(article, data=request.data, partial=True)

        if article_serializer.is_valid():
            article_serializer.save()
            return Response({"message": "게시글이 수정 되었습니다."}, status=status.HTTP_200_OK)
        return Response(article_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, article_id):
        user = request.user.id
        article = ArticleModel.objects.get(id=article_id)
        if article.user.id == user:
            article.delete()
            return Response({"message": "해당 게시글이 삭제 되었습니다."}, status=status.HTTP_200_OK)
        else :
            return Response({"message": "게시글 작성자가 아닙니다"}, status=status.HTTP_400_BAD_REQUEST)
        
        
class CommentView(APIView):
    def get(self, request):
        comment = ArticleCommentModel.objects.all()
        serialized_data = CommentSerializer(comment, many=True).data

        return Response(serialized_data, status=status.HTTP_200_OK)
    
    def post(self, request, article_id):
        request.data["user"] = request.user.id
        comment = ArticleModel.objects.get(id=article_id)
        
        data = {
            "user": request.user.id,
            "article": comment.id,
            "comment": request.data["comment"]
        }
        comment_serializer = CommentSerializer(data=data)
        print(f'ㅡㅡㅡㅡㅡㅡ{data["comment"]} ㅡㅡㅡㅡㅡㅡㅡ')
        if data["comment"] in ["바보", "해삼", "멍게", "말미잘"]:
            return Response({"message": "부정적인 댓글을 감지하였습니다."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            comment_serializer.is_valid()
            comment_serializer.save()
            return Response({"message": "댓글작성이 완료되었습니다."}, status=status.HTTP_200_OK)
    
    def put(self, request, commnet_id):
        comment = ArticleCommentModel.objects.get(id=commnet_id)
        comment_serializer = CommentSerializer(comment, data=request.data, partial=True)
        
        if comment_serializer.is_valid():
            comment_serializer.save()
            return Response({"message": "수정이 완료되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response(comment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, commnet_id):
        user = request.user.id
        comment = ArticleCommentModel.objects.get(id=commnet_id)
        
        if comment.user.id == user:
            comment.delete()
            return Response({"message": "댓글이 삭제되었습니다."}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "댓글 작성자가 아닙니다."}, status=status.HTTP_400_BAD_REQUEST)


class LikeView(APIView):
    def get(self, request):
        like = LikeModel.objects.all()
        serialized_data = LikeSerializer(like, many=True).data
        
        return Response(serialized_data, status=status.HTTP_200_OK)
    
    def post(self, request, like_id):
        request.data["user"] = request.user.id
        request.data["article"] = like_id
        like_serializer = LikeSerializer(data=request.data)
        existed_like = LikeModel.objects.filter(
            Q(user_id=request.user.id) & Q(article_id=like_id)
        )
        
        if existed_like:
            existed_like.delete()
            return Response({"message": "좋아요를 취소 했습니다."}, status=status.HTTP_200_OK)
        
        elif like_serializer.is_valid():
            like_serializer.save()
            return Response({"message": "좋아요를 클릭 했습니다."}, status=status.HTTP_200_OK)