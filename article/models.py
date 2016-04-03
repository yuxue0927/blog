# -*- coding: utf-8 -*-

from django.db import models
from django.core.urlresolvers import reverse
#from django.contrib.sites.models import Site

# Create your models here.

class Tag(models.Model):
    tag_name = models.CharField("标签",max_length=64)
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'
    def __unicode__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField("主题",max_length = 100)  #博客题目
    category = models.CharField("分类",max_length = 50, blank = True)  #博客分类 可为空
    tag = models.ManyToManyField(Tag, blank=True)  # 博客标签 可为空
    date_time = models.DateTimeField("日期",auto_now_add = True)  #博客日期
    content = models.TextField("正文",blank = True, null = True)  #博客文章正文

    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path

    def __unicode__(self) :
        return self.title

    class Meta:
        verbose_name = '主题'
        verbose_name_plural = '文章'
        ordering = ['-date_time']

