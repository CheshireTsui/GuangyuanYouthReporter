# -*- coding: UTF-8 -*-
from django.db import models
from django.contrib import admin
from youth.settings import  MEDIA_ROOT
from News.models import  Article

class Cover(models.Model):
    image = models.FileField(upload_to="home_page_cover/")

    class Meta: 
        ordering = ['-id']

    def __unicode__(self):
        return self.image.name

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
                                                                    (self.image.name, self.image.name))
    thumbnail.allow_tags = True


class Top(models.Model):
    name = models.CharField(max_length=64)
    school = models.ForeignKey(Article)
    amount = models.IntegerField(default=0)

    class Meta: 
        ordering = ['-amount']

    def __unicode__(self):
        return self.name


class Star_of_the_Week(models.Model):
    name = models.CharField(max_length=64)
    image = models.FileField(upload_to="star_of_the_week/")

    class Meta: 
        ordering = ['-id']

    def __unicode__(self):
        return self.name

    def thumbnail(self):
        return """<a href="/media/%s"><img border="0" alt="" src="/media/%s" height="40" /></a>""" % (
                                                                    (self.image.name, self.image.name))
    thumbnail.allow_tags = True


class CoverAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","thumbnail",]

class TopAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","amount","school",]

class StarAdmin(admin.ModelAdmin):
    list_display = ["__unicode__","thumbnail",]


admin.site.register(Cover,CoverAdmin)
admin.site.register(Top,TopAdmin)
admin.site.register(Star_of_the_Week,StarAdmin)