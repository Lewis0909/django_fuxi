from django.conf.urls import url
from user.views import index,bookList,bookinfo,bookpage,views,param,keys,jsonresponse,response,CenterView,BookView

app_name='user'

# 固定写法
urlpatterns = [
    url(r'^$',index),

    # 书籍页面url配置
    url(r'^booklist/$',bookList),

    # 数据库操作
    url(r'^bookinfo/$',bookinfo),

    # 分页
    url(r'^bookpage/$',bookpage),

    #　视图
    url(r'^views/$',views),

    # 位置参数
    url(r'^param/(\d+)/(\d+)/$',param),

    # 关键字参数
    url(r'^(?P<name>\w+)/(?P<sex>\w+)/$',keys),

    # json响应
    url(r'^json/$',jsonresponse,name='test'),

    # 重定向
    url(r'^redirect/$',response),


    url(r'^login/$',BookView.as_view()),

    # 类视图函数url
    url(r'^center/$',CenterView.as_view())

    # 这是经理的代码
]
