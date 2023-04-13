from django.db import models
from django.conf import settings

class Board(models.Model):
    # qna_no = Board.pk // 모델의 pk와 동일
    qna_title = models.CharField(max_length=300,null=False)
    qna_date = models.DateTimeField(auto_now_add=True,null=False)
    user_id = models.CharField(max_length=15,null=False)
    qna_content = models.CharField(max_length=3000,null=False)

class Comment(models.Model):
    # com_no = Comment.pk // 모델의 pk와 동일
    qna_no = models.ForeignKey(Board,on_delete=models.CASCADE) # 게시물 <-> 댓글 , 1:N 관계 지정
    com_date = models.DateTimeField(auto_now_add=True,null=False) 
    user_id = models.CharField(max_length=15,null=False)
    com_comment = models.CharField(max_length=3000,null=False)