from django.conf.urls import url
from . import views

urlpatterns = [
    # 首页
    url(r'^$', views.indexView.as_view(), name='index'),
    # 文章内容页面
    url(r'^single/(?P<article_id>\d+)$', views.singleView.as_view(), name='single'),
    # 文章列表页面
    url(r'^list/(?P<type_id>\d+)$', views.listView.as_view(), name='list'),
    # 关于页面
    url(r'^about$', views.aboutView.as_view(), name='about'),
    # 联系页面
    url(r'^contact$', views.contactView.as_view(), name='contact'),
]

