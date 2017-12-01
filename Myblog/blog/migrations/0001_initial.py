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
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('title', models.CharField(verbose_name='文章标题', max_length=40)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('digest', models.CharField(verbose_name='文章摘要', max_length=256)),
                ('content', tinymce.models.HTMLField(verbose_name='文章内容', blank=True)),
                ('path', models.ImageField(verbose_name='文章配图', upload_to='blog/')),
                ('author', models.CharField(verbose_name='文章作者', max_length=20)),
                ('emphasis', models.BooleanField(verbose_name='重点标记', default=False)),
            ],
            options={
                'verbose_name': '文章',
                'db_table': 'df_article',
                'verbose_name_plural': '文章',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('comment', models.CharField(verbose_name='评论', max_length=256)),
                ('name', models.CharField(verbose_name='评论人', max_length=20)),
                ('email', models.CharField(verbose_name='邮箱', max_length=40)),
                ('site', models.CharField(verbose_name='评论人站点', max_length=40)),
                ('article', models.ForeignKey(verbose_name='对应文章', to='blog.Article')),
            ],
            options={
                'verbose_name': '评论',
                'db_table': 'df_comment',
                'verbose_name_plural': '评论',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('message', models.CharField(verbose_name='message', max_length=256)),
                ('name', models.CharField(verbose_name='联系人姓名', max_length=20)),
                ('email', models.CharField(verbose_name='邮箱', max_length=40)),
            ],
            options={
                'verbose_name': '联系人',
                'db_table': 'df_contact',
                'verbose_name_plural': '联系人',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('update_time', models.DateTimeField(verbose_name='更新时间', auto_now=True)),
                ('is_delete', models.BooleanField(verbose_name='删除标记', default=False)),
                ('create_time', models.DateTimeField(verbose_name='创建时间', auto_now_add=True)),
                ('name', models.CharField(verbose_name='类型名称', max_length=20)),
            ],
            options={
                'verbose_name': '文章类型',
                'db_table': 'df_genre',
                'verbose_name_plural': '文章类型',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ForeignKey(verbose_name='文章类型', to='blog.Genre'),
        ),
    ]
