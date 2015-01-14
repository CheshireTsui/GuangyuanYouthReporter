# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from News.models import *
from models import *

class News():
    """docstring for ClassName"""
    def __init__(self, title, img):
        self.news = title
        self.image = img


def index(request):
    cover_list = Cover.objects.all()
    top_list = Top.objects.all()
    star_list = Star_of_the_Week.objects.all()
    star = star_list[0]

    news_all = Column.objects.get(name="校园新闻").article.all()
    news_list = []
    for i in news_all:
    	img = i.image.all()
    	news = News(i,img[0])
    	news_list.append(news)

    return render_to_response('index.html',{'cover':cover_list, 'top':top_list, 'star':star, 'news':news_list,})