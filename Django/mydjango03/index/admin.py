from django.contrib import admin
from .models import *


# 声明author的高级管理类 -- AuthorAdmin
class AuthorAdmin(admin.ModelAdmin):
    # list_display = : 定义在列表页上显示的字段
    list_display = ("name", "age", "email")

    # list_display_links = 定义在列表页中能链接到详情页中
    list_display_links = ("name", "email")

    # list_editable : 定义在列表页中就可以编辑的字段们,
    #### 注意 list_editable 和 list_editable 里面的字段不能同时出现
    list_editable = ("age",)

    # list_filter 作用：列表页右侧增加一个过滤器快速筛选
    list_filter = ("isActive",)

    # search_fields 作用：添加允许被搜索的字段们
    search_fields = ("name",)

    # fields 作用：在详情页中，指定要显示的字段以及顺序
    # fields = ("email", "name")

    # fieldsets 作用：详情页中，对字段们进行分组
    #######: fieldsets与fields不能共存的
    fieldsets = (
        # 分组1
        (
            "基本选项",
            {
                "fields": ("email", "name"),
            }
        ),

        # 分组2
        (
            "可选选项",
            {
                'fields': ("age", "isActive"),
                'classes':("collapse",)
            }
        )

    )


class BookAdmin(admin.ModelAdmin):
    # date_hierarchy作用：列表页中增加时间分层选择器
    date_hierarchy = "publicate_date"


class PublisherAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "city")
    list_editable = ("address", "city")
    list_filter = ("city",)
    search_fields = ("name", "webdite")
    fieldsets = (
        ("基本信息",
        {
            "fields":("name","address","city"),
        }),
        ("高级信息",
        {
            "fields":("country", "webdite"),
            "classes":("collapse",)
        }),
    )




# Register your models here.

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Wife)
