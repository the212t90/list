from django.db import models
from django.conf import settings
# Create your models here.


class Book(models.Model):
    """書籍"""
    book = models.CharField('書籍名', max_length=255)
    author = models.CharField('著者名', max_length=255, blank=True)
    publisher = models.CharField('出版社', max_length=255, blank=True)
    year = models.CharField('発行年', max_length=20,blank=True)
    page = models.CharField('ページ数', max_length=20,blank=True)
    remarks = models.TextField('備考',max_length=1000,blank=True)

    def __str__(self):
        return self.book

class Reference(models.Model):
    """論文"""
    reference = models.CharField("タイトル", max_length=255)
    site = models.CharField('サイト', max_length=255, blank=True)
    url = models.CharField("URL", max_length=500, blank=True)
    day = models.CharField("閲覧日", max_length=50,blank=True)
    remarks_ref = models.TextField('備考',max_length=1000,blank=True)


    def __str__(self):
        return self.reference