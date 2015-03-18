#! coding:utf-8
from django.shortcuts import render,render_to_response,HttpResponseRedirect
from django.http import Http404
from blog import models
from form import CommentForm
from models import Article
import hashlib
# Create your views here.
def index(request):
    article_list = models.Article.objects.order_by('-stime')
    return render_to_response('index.html',{'article_list':article_list})

def detail(request,article_id):
    try:
        article = models.Article.objects.get(pk=article_id)#pk=id
        comment_list = models.Comment.objects.all()
    except models.Article.DoesNotExist:
        raise Http404

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog/%s/'%article_id)
    else:
        form = CommentForm()
    return render_to_response('detail.html',{'article':article,'comment_list':comment_list,'form':form})


def add_like(request,article_id):
    ctime = Article.objects.get(id=article_id).stime
    hash_id = hashlib.sha1(str(ctime)).hexdigest()
    try:
        if hash_id in str(request.COOKIES.get(article_id)):
            return HttpResponseRedirect('/blog/%s/like.html'%article_id)
        else:
            article = Article.objects.get(id=article_id)
            article.likes +=1
            article.save()
            response = HttpResponseRedirect('/blog/%s/'%article_id)
            response.set_signed_cookie(article_id,value=hash_id,max_age=86400)
            return response
    except models.Article.DoesNotExist:
            raise Http404
