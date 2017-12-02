# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('title', models.CharField(max_length=40, verbose_name='文章标题')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('digest', models.CharField(max_length=256, verbose_name='文章摘要')),
                ('content', tinymce.models.HTMLField(blank=True, verbose_name='文章内容')),
                ('path', models.ImageField(upload_to='blog/', verbose_name='文章配图')),
                ('author', models.CharField(max_length=20, verbose_name='文章作者')),
                ('emphasis', models.BooleanField(default=False, verbose_name='重点标记')),
            ],
            options={
                'db_table': 'df_article',
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('comment', models.CharField(max_length=256, verbose_name='评论')),
                ('name', models.CharField(max_length=20, verbose_name='评论人')),
                ('email', models.CharField(max_length=40, verbose_name='邮箱')),
                ('site', models.CharField(max_length=40, verbose_name='评论人站点')),
                ('article', models.ForeignKey(to='blog.Article', verbose_name='对应文章')),
            ],
            options={
                'db_table': 'df_comment',
                'verbose_name_plural': '评论',
                'verbose_name': '评论',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('message', models.CharField(max_length=256, verbose_name='message')),
                ('name', models.CharField(max_length=20, verbose_name='联系人姓名')),
                ('email', models.CharField(max_length=40, verbose_name='邮箱')),
            ],
            options={
                'db_table': 'df_contact',
                'verbose_name_plural': '联系人',
                'verbose_name': '联系人',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='删除标记')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('name', models.CharField(max_length=20, verbose_name='类型名称')),
            ],
            options={
                'db_table': 'df_genre',
                'verbose_name_plural': '文章类型',
                'verbose_name': '文章类型',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ForeignKey(to='blog.Genre', verbose_name='文章类型'),
        ),
    ]
