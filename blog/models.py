#! coding:utf-8
from django.db import models

# Create your models here.

class Tag(models.Model):
    tags = models.CharField(max_length=150)
    def __unicode__(self):
        return  self.tags
    class Meta:
        verbose_name = '标签'
        verbose_name_plural = '标签'



class Article(models.Model):
    title = models.CharField(max_length=150)
    body  = models.TextField()
    stime = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=True)
    likes = models.IntegerField(default=0)

    tags = models.ManyToManyField(Tag)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name_plural = '博客'
        verbose_name = '博客'
        ordering = ['-stime']


class Comment(models.Model):
    name = models.CharField(max_length=150)
    mail = models.EmailField()
    stime = models.DateTimeField(auto_now=True)
    body = models.TextField()
    article = models.ForeignKey(Article)

    def __unicode__(self):
        return self.name+"("+self.mail+"):"+self.body
    class Meta:
        verbose_name = "评论"
        verbose_name_plural="评论"
        ordering=['-stime']

