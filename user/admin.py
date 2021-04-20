from django.contrib import admin
# 导入模型
from user.models import BookInfo,PeopleInfo

# Register your models here.

# 注册书籍模型
admin.site.register(BookInfo)
# 注册人物模型
admin.site.register(PeopleInfo)