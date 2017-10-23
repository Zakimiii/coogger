from django.http import *
from django.shortcuts import render
from django.contrib.auth import *
from django.contrib import messages
from django.db.models import F
from cooggerapp.models import Blog
from cooggerapp.views import tools
from django.db.models import Q

def hashtag(request,hashtag):
    queryset = Blog.objects.filter(tag__regex = hashtag)
    username = request.user.username
    blogs = tools.paginator(request,queryset,10)
    paginator = blogs
    pp = tools.get_pp(blogs)
    stars = []
    for i in blogs:
        try:
            stars.append(str(int(i.stars/i.hmstars)+1))
        except ZeroDivisionError:
            stars.append("0")
    blogs = zip(blogs,pp,stars)
    tools_topic = tools.Topics()
    category = tools_topic.category
    elastic_search = dict(
     title ="#"+hashtag+" | coogger",
     keywords = hashtag,
     description = hashtag +" konu etiketi altında ki bütün coogger bilgilerini gör",
    )
    output = dict(
        blog = blogs,
        nav_category = category,
        general = True,
        username = username,
        paginator = paginator,
        elastic_search = elastic_search,
    )
    return render(request,"blog/blogs.html",output)

def list(request,list):
    queryset = Blog.objects.filter(content_list = list)
    username = request.user.username
    blogs = tools.paginator(request,queryset,10)
    paginator = blogs
    pp = tools.get_pp(blogs)
    stars = []
    for i in blogs:
        try:
            stars.append(str(int(i.stars/i.hmstars)+1))
        except ZeroDivisionError:
            stars.append("0")
    blogs = zip(blogs,pp,stars)
    tools_topic = tools.Topics()
    category = tools_topic.category
    elastic_search = dict(
     title = list +" | coogger",
     keywords = list,
     description = list +" liste etiketi altında ki bütün coogger bilgilerini gör",
    )
    output = dict(
        blog = blogs,
        nav_category = category,
        general = True,
        username = username,
        paginator = paginator,
        elastic_search = elastic_search,
    )
    return render(request,"blog/blogs.html",output)