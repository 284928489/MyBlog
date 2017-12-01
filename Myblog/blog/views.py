from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.views.generic import View
from blog.models import Genre, Article, Comment, Contact
import re

# Create your views here.
class indexView(View):
    '''首页'''
    def get(self, request):
        '''请求首页'''
        articles = Article.objects.all().order_by('-update_time')
        articles_1 = articles[:2]
        articles_2 = articles[2:4]
        tags = Genre.objects.all()
        related_post = Article.objects.filter(type_id=1)
        featured_post = Article.objects.filter(emphasis=True)
        context = {'articles_1':articles_1,
                   'articles_2':articles_2,
                   'tags':tags,
                   'related_post':related_post,
                   'featured_post':featured_post}
        return render(request,'index.html', context)

class singleView(View):
    '''文章内容'''
    def get(self, request, article_id):
        '''请求文章内容'''
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return redirect(reverse('blog:index'))
        comments = Comment.objects.filter(article_id=article_id)
        comment_count = len(comments)
        context = {'article':article,
                   'comments':comments,
                   'comment_count':comment_count}
        return render(request, 'single.html', context)
    def post(self, request, article_id):
        '''文章评论功能'''
        article_id = article_id
        try:
            article = Article.objects.get(id=article_id)
        except Article.DoesNotExist:
            return redirect(reverse('blog:index'))
        comment = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        if not all([name,email,website,comment]):
            comments = Comment.objects.filter(article_id=article_id)
            comment_count = len(comments)
            context = {'article':article,
                       'comments':comments,
                       'comment_count':comment_count,
                       'errmsg':'数据不完整'}
            # 数据不完整
            return render(request, 'single.html', context)
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            comments = Comment.objects.filter(article_id=article_id)
            comment_count = len(comments)
            context = {'article':article,
                       'comments':comments,
                       'comment_count':comment_count,
                       'errmsg':'邮箱不合法'}
            return render(request, 'single.html', context)
        temp_comment = Comment(comment=comment,email=email,name=name,site=website,article=article)
        temp_comment.save()
        comments = Comment.objects.filter(article_id=article_id)
        comment_count = len(comments)
        context = {'article':article,
                   'comments':comments,
                   'comment_count':comment_count}
        return render(request, 'single.html', context)

class listView(View):
    '''文章列表视图'''
    def get(self,request,type_id):
        articles = Article.objects.filter(type=type_id)
        tags = Genre.objects.all()
        related_post = Article.objects.filter(type_id=type_id)
        featured_post = Article.objects.filter(emphasis=True)
        context = {'articles_1':articles,
                   'tags':tags,
                   'related_post':related_post,
                   'featured_post':featured_post}
        return render(request,'index.html',context)

class aboutView(View):
    '''关于视图'''
    def get(self,request):
        return render(request,'about.html')

class contactView(View):
    '''联系视图'''
    def get(self,request):
        return render(request,'contact.html')
    def post(self,request):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        if not all([name,email,message]):
            return render(request,'contact.html', {'errmsg':'数据不完整'})
        if not re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email):
            return render(request, 'contact.html', {'errmsg':'邮箱不合法'})
        temp_data = Contact(name=name,email=email,message=message)
        temp_data.save()
        return render(request,'contact.html')

