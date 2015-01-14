# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from youth.settings import  MEDIA_ROOT
import random

class Image(models.Model):
    title = models.CharField(max_length=64)
    image = models.FileField(upload_to="news_images/")

    class Meta: 
        ordering = ['-id']

    def __unicode__(self):
        return self.image.name

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
                                                                    (self.image.name, self.image.name))
    thumbnail.allow_tags = True


class Article(models.Model):
    title = models.CharField(max_length=64)
    intro = models.CharField(max_length=100)
    image = models.ManyToManyField(Image,blank=True)
    content = models.TextField()
    source = models.CharField(max_length=10, default="本站原创")
    editor = models.CharField(max_length=10)
    uptime = models.DateTimeField(auto_now=True)
    icon = models.IntegerField(default=int(random.uniform(1, 19)))
    rating = models.IntegerField(default=0)

    class Meta: 
        ordering = ['-id']

    def __unicode__(self):
        return self.title


class Column(models.Model):
    name = models.CharField(max_length=32)
    article = models.ManyToManyField(Article,blank=True)

    class Meta: 
        ordering = ['-id']

    def __unicode__(self):
        return self.name


class ImageAdmin(admin.ModelAdmin):
    list_display = ["title","thumbnail",]

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","intro","uptime",]

class ColumnAdmin(admin.ModelAdmin):
    list_display = ["name",]


admin.site.register(Image,ImageAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Column,ColumnAdmin)