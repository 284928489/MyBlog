from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class Genre(models.Model):
    '''文章类型模型类'''
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    name = models.CharField(max_length=20,verbose_name='类型名称')

    class Meta:
        db_table = 'df_genre'
        verbose_name = '文章类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Article(models.Model):
    '''文章模型类'''
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    title = models.CharField(max_length=40, verbose_name='文章标题')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    digest = models.CharField(max_length=256, verbose_name='文章摘要')
    content = HTMLField(blank=True, verbose_name='文章内容')
    path = models.ImageField(upload_to='blog/', verbose_name='文章配图')
    type = models.ForeignKey('Genre', verbose_name='文章类型')
    author = models.CharField(max_length=20, verbose_name='文章作者')
    emphasis = models.BooleanField(default=False, verbose_name='重点标记')


    class Meta:
        db_table = 'df_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title + '------' + str(self.create_time)

class Comment(models.Model):
    '''评论模型类'''

    CAPTAIN_INFO= {
        'name':'shaodi',
        'site':'kaleka',
        'email':'fengzhong_yue@163.com',
    }

    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    comment = models.CharField(max_length=256, verbose_name='评论')
    name = models.CharField(max_length=20, verbose_name='评论人')
    email = models.CharField(max_length=40, verbose_name='邮箱')
    site = models.CharField(max_length=40, verbose_name='评论人站点')
    article = models.ForeignKey('Article', verbose_name='对应文章')

    class Meta:
        db_table = 'df_comment'
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.article + self.name

class Contact(models.Model):
    '''联系模型类'''
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    message = models.CharField(max_length=256, verbose_name='message')
    name = models.CharField(max_length=20, verbose_name='联系人姓名')
    email = models.CharField(max_length=40, verbose_name='邮箱')

    class Meta:
        db_table = 'df_contact'
        verbose_name = '联系人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name + str(self.create_time)
