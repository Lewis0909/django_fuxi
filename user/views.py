from django.shortcuts import render,redirect
# 导入HttpResponse模块
from django.http import HttpResponse, JsonResponse
from django.urls import reverse

from user.models import BookInfo, PeopleInfo
# 导入分页类
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# Create your views here.

# 定义响应视图函数
def index(request):
    context = request.GET
    print(context.get('value1'))
    context = {"title": "这是后端传过来的数据"}

    return render(request, 'user/index.html',context)
    # return HttpResponse('ok')


# 提供书籍列表信息
def bookList(request):

    # 查询书籍数据
    book = BookInfo.objects.all()

    # 组装返回数据
    context = {"books" : book}

    return render(request, 'user/index/booklist.html', context)

# 数据库操作
def bookinfo(request):

    # save()
    book = BookInfo(
        name='python_django 复习',
        pub_date='2021-04-02'
    )
    book.save()
    # print(book)

    # create()
    PeopleInfo.objects.create(
        name = 'itheima',
        book = book
    )

    return HttpResponse('OKKKK')

# 分页
def bookpage(request):
    # 查询数据
    books = BookInfo.objects.all().order_by('-id')
    print(books)

    # 创建分页实例
    paginator = Paginator(books, 2)
    print(paginator)

    # 获取指定页码的数据
    page_skus = paginator.page(1)
    for book in page_skus:
        print(book)

    # 获取分页数据
    total_page = paginator.num_pages
    print(total_page)

    if page_skus.has_next():

        print('true')
        print(page_skus.next_page_number())

    if page_skus.has_previous():
        print('true')
        print(page_skus.previous_page_number())



    return HttpResponse('OK')

# 视图
def views(request):
    return  HttpResponse('odik')

# 位置参数
def param(request, value1, value2):
    context = {"value1":value1, "value2":value2}
    return HttpResponse(context)

# 关键字参数
def keys(request, value1, value2):
    context = {"value1": value1, "value2": value2}
    # context = request.GET
    print(context)
    return HttpResponse(context)

# JsonResponse
def jsonresponse(request):
    return  JsonResponse({"city":'beijing',"subject":"python"})

# redirect
def response(request):
    # path = reverse('test')
    path = reverse('user:test')
    return  redirect(path)
    # return redirect('/json/')

class BookView(View):

    def get(self,request):

        return HttpResponse('get')


    def post(self,request):

        return HttpResponse('post')


    def put(self,request):

        return HttpResponse('put')

    def oooo(self,request):

        return HttpResponse('oooo')

class CenterView(LoginRequiredMixin,View):
    def get(self, request):
        return HttpResponse('个人中心展示')

    def post(self, request):
        return HttpResponse('个人中心修改')