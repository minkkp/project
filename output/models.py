from django.db import models

class Upload(models.Model):
    # upload_no = Upload.pk // 모델의 pk와 동일
    user_id = models.CharField(max_length=15,null=False)
    img_name = models.CharField(max_length=128,null=False)
    img_file = models.ImageField(upload_to="images/", blank=True)
    update_date = models.DateTimeField(auto_now_add=True,null=False)