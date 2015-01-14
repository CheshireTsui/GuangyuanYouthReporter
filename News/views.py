# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import *

class News():
    """docstring for ClassName"""
    def __init__(self, title, img):
        self.news = title
        self.image = img


def composeArticle(news_list, n = 6):
    list_this = []
    if len(news_list) < n:
        length = len(news_list) / 2
        if len(news_list) % 2 == 1:
            length += 1
    else:
        length = n/2
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
    for i in raw_list:
        img = i.image.all()
        news = News(i,img[0])
        imgs_list.append(news)

    shooting_list = composeImage(shooting_all)
    idea_list = composeArticle(idea_all)
    return render_to_response('literature.html',{'shooting':shooting_list, 'list':idea_list, 'img':imgs_list,})


def Reporter(request):
    news_all = Column.objects.get(name="小记者课堂").article.all()
    imgs_all = Column.objects.get(name="小记者风采").article.all()
    news_list = composeArticle(news_all)
    imgs_list = composeImage(imgs_all)
    try:
        a1 = Article.objects.get(title="小记者报名")
        a2 = Article.objects.get(title="我要投稿")
    except Exception, e:
        a1 = '#'
        a2 = '#'  
    return render_to_response('reporter.html',{'list':news_list, 'shooting':imgs_list, 'a1':a1, 'a2':a2,})


def Content(request):
    news_id = request.GET.get('news_id')
    try:
        news = Article.objects.get(id=news_id)
        img = news.image.all()
        img = img[0]
    except Exception, e:
        return HttpResponse("%s 请求的文章不存在！"%e)
    return render_to_response('text.html',{'news':news, 'img':img,})


def ArticleList(request):
    news_column = request.GET.get('news_column')
    if (not request.GET.get('news_page'))or(request.GET.get('news_page')==0):
        news_page = 1
    else:
        news_page = int(request.GET.get('news_page'))
    title = ''
    if news_column:
        if news_column == 'left-behind': 
            news_all = Column.objects.get(name="留守之家").article.all()
            title = "留守之家 <i class=\"fa fa-slideshare\"></i>"
        elif news_column == 'news': 
            news_all = Column.objects.get(name="校园新闻").article.all()
            title = "校园新闻 <i class=\"fa fa-slideshare\"></i>"
        elif news_column == 'shooting': 
            news_all = Column.objects.get(name="我爱拍客").article.all()
            title = "我爱拍客 <i class=\"fa fa-camera\"></i>"
        elif news_column == 'imagine': 
            news_all = Column.objects.get(name="奇思妙想").article.all()
            title = "奇思妙想 <i class=\"fa fa-lightbulb-o\"></i>"
        elif news_column == 'class': 
            news_all = Column.objects.get(name="小记者课堂").article.all()
            title = "小记者课堂 <i class=\"fa fa-key\"></i>"
        elif news_column == 'reporter': 
            news_all = Column.objects.get(name="小记者风采").article.all()
            title = "小记者风采 <i class=\"fa fa-file-image-o\"></i>"
        else: 
            news_all = Article.objects.all()
            title = "全部新闻 <i class=\"fa fa-university\"></i>"
    else:
        news_all = Article.objects.all()
        title = "全部新闻 <i class=\"fa fa-university\"></i>"

    cnt = len(news_all)/10
    if len(news_all)%10!=0: cnt += 1
    cnt = range(1,cnt+1)

    try:
        news_all = news_all[(news_page-1)*10:news_page*10]
    except Exception, e:
        news_all = news_all[(news_page-1)*10:]
    news_list = composeArticle(news_all,10)

    return render_to_response('article-list.html',{'title':title,'list':news_list, 'cnt':cnt, 'news_column':news_column, 'former':news_page-1,'later':news_page+1,})