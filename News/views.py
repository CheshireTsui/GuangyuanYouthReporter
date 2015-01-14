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
    news_all = Column.objects.get(name="留守之家").article.all()
    news_list = composeArticle(news_all)
    return render_to_response('left-behind.html',{'list':news_list,})


def NewsList(request):
    news_all = Column.objects.get(name="校园新闻").article.all()
    imgs_all = Column.objects.get(name="魅力校园").article.all()
    news_list = composeArticle(news_all)
    imgs_list = composeImage(imgs_all)
    return render_to_response('news.html',{'list':news_list, 'school':imgs_list,})


def Literature(request):
    shooting_all = Column.objects.get(name="我爱拍客").article.all()
    idea_all = Column.objects.get(name="奇思妙想").article.all()
    imgs_list = []
    raw_list = Column.objects.get(name="书画廊").article.all()
    for x in raw_list:
        img = x.image.all()
        imgs_list.append(img[0])

    shooting_list = composeImage(shooting_all)
    idea_list = composeArticle(idea_all)
    return render_to_response('literature.html',{'shooting':shooting_list, 'list':idea_list, 'img':imgs_list,})
