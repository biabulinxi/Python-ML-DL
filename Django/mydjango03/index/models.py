from django.db import models


# Create your models here.

# 创建一个实体类 -- Publisher 表示出版社
# 注意：主键&自增列，在Django ORM 中会自动创建

class Publisher(models.Model):
    """
    name:出版社名称 -- varchar
    address:地址 -- varchar
    city: 城市 -- varchar
    country: 国家 -- varchar
    website：网址 -- varchar
    """
    name = models.CharField(max_length=30, verbose_name='出版商')
    address = models.CharField(max_length=100, verbose_name="地址")
    city = models.CharField(max_length=20, verbose_name="城市")
    country = models.CharField(max_length=20, verbose_name="国家")
    webdite = models.URLField(verbose_name="网址")

    # 重写方法 __str__()
    def __str__(self):
        return self.name

    class Meta:
        db_table = "publisher"
        verbose_name = "出版社"
        verbose_name_plural = verbose_name


class Author(models.Model):
    """
    1.name - 姓名
    2.age - 年龄
    3.email - 邮箱(允许为空)
    """
    name = models.CharField(max_length=30, unique=True, db_index=True, verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True, verbose_name='邮箱')
    isActive = models.BooleanField(default=True, verbose_name='激活')

    # 重写方法 __str__()
    def __str__(self):
        return self.name

    # 内部类 meta 修改在后台的展现形式
    class Meta:
        db_table = "author"
        verbose_name = "作者"
        verbose_name_plural = verbose_name


class Book(models.Model):
    """
    1.title - 书名
    2.publicate_date - 出版时间
    """
    title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name="书名")
    publicate_date = models.DateTimeField(db_index=True, verbose_name="出版日期")
    # 增加对publisher 的一对多引用
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,null=True)

    # 添加对Author的多对多的引用
    authors = models.ManyToManyField(Author)


    def __str__(self):
        return self.title

    class Meta:
        db_table = "book"
        verbose_name = "书籍"
        verbose_name_plural = verbose_name


class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    author = models.OneToOneField(Author, on_delete=models.CASCADE)

