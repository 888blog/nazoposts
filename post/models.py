from django.conf import settings
from django.db import models
from django.utils import timezone
import uuid

class Post(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タイトル', max_length=50)
    question = models.CharField(verbose_name='問題文', max_length=200)
    q_img1 = models.ImageField(verbose_name='問題画像1', upload_to='documents/', blank=True, null=True)
    q_img2 = models.ImageField(verbose_name='問題画像2', upload_to='documents/', blank=True, null=True)
    q_img3 = models.ImageField(verbose_name='問題画像3', upload_to='documents/', blank=True, null=True)
    q_img4 = models.ImageField(verbose_name='問題画像4', upload_to='documents/', blank=True, null=True)
    answer = models.CharField(verbose_name='答え', max_length=100)
    explanation = models.CharField(verbose_name='解説', max_length=200)
    e_img1 = models.ImageField(verbose_name='解説画像1', upload_to='documents/', blank=True, null=True)
    e_img2 = models.ImageField(verbose_name='解説画像2', upload_to='documents/', blank=True, null=True)
    e_img3 = models.ImageField(verbose_name='解説画像3', upload_to='documents/', blank=True, null=True)
    e_img4 = models.ImageField(verbose_name='解説画像4', upload_to='documents/', blank=True, null=True)
    good = models.IntegerField(verbose_name='高評価', default=0)
    bad = models.IntegerField(verbose_name='低評価', default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name='作成日時', default=timezone.now)
    published_at = models.DateTimeField(verbose_name='投稿日時', blank=True, null=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', default=timezone.now)
    