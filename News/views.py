# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *

class News():
    """docstring for ClassName"""
    def __init__(self, title, img):
        self.news = title
        self.image = img


def composeArticle(news_list):
    list_this = []
    if len(news_list) < 6:
        length = len(news_list) / 2
        if len(news_list) % 2 == 1:
            length += 1
    else:
        length = 3
    for i in range(0,length):
        box = []
        box.append(news_list[i * 2])
        try:
            box.append(news_list[i * 2 + 1])
        except Exception, e:
            box.append(None)
        list_this.append(box)
    return list_this


def composeImage(raw_list):
    list_this = []
    news_list = []
    for i in raw_list:
        img = i.image.all()
        news = News(i,img[0])
        news_list.append(news)

    if len(news_list) <= 3:
        length = 1
    else:
        length = 2
    for i in range(0,length):
        box = []
        try:
            box.append(news_list[i * 3])
        except Exception, e:
            box.append(None)
        try:
            box.append(news_list[i * 3 + 1])
        except Exception, e:
            box.append(None)
        try:
            box.append(news_list[i * 3 + 2])
        except Exception, e:
            box.append(None)
        list_this.append(box)
    #return HttpResponse(list_this)
    return list_this


def LeftBehind(request):
    news_all = Column.objects.get(name="校园新闻").article.all()
    news_list = composeArticle(news_all)
    return render_to_response('left-behind.html',{'list':news_list,})
