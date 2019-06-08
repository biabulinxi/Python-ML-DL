# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/27 11:27
# @File_name:01_dicVectorize.py
# @IDE:PyCharm

"""
特征值转换，文本特征处理
"""

from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import jieba


def dictvec():
    """
    z字典数据抽取
    :return:
    """

    # 实例化, 返回sparse稀疏矩阵，节约内存，方便读取处理, 默认True
    dicv = DictVectorizer(sparse=False)

    # 调用fit_transform,
    data = dicv.fit_transform([
        {'city': '北京', 'temperature': 100},
        {'city': '上海', 'temperature': 80},
        {'city': '广州', 'temperature': 90},
    ])

    print(dicv.get_feature_names())  # 类似列名数组，['city=上海', 'city=北京', 'city=广州', 'temperature']

    print(data)

    print(dicv.inverse_transform(data))

    return None


def countvec():
    """
    对文本进行特征值化, 统计英文单词出现的次数，单个英文单词不进行统计转换，默认空格进行拆分识别
    :return:
    """
    cv = CountVectorizer()
    data = cv.fit_transform(
        ["生活好难 the last column ('Class') the the the  in in in", "Simply 谢谢啦 t to obtain features columns"])
    print(data)
    print(cv.get_feature_names())
    print(data.toarray())  # 将sparse矩阵转成数组


def cutword():
    """
    进行jieba分词, 结巴分词返回的是生成器
    :return:
    """
    con1 = jieba.cut("今天很残酷，明天更残酷，后天很美好，但绝对大部分是死在明天晚上，所以每个人不要放弃今天。")
    con2 = jieba.cut("我们看到的从很远星系来的光是在几百万年之前发出的，这样当我们看到宇宙时，我们是在看它的过去。")
    con3 = jieba.cut("如果只用一种方式了解某样事物，你就不会真正了解它。了解事物真正含义的秘密取决于如何将其与我们所了解的事物相联系。")

    # 装换成列表
    content1 = list(con1)
    content2 = list(con2)
    content3 = list(con3)

    print(con1)
    print(content1)

    # 把列表转换成字符串,用空格隔开
    c1 = ' '.join(content1)
    c2 = ' '.join(content2)
    c3 = ' '.join(content3)
    return c1, c2, c3


def hanzivec():
    """
    中文字符特征化
    :return:
    """
    c1, c2, c3 = cutword()
    print(c1,c2,c3)

    cv = CountVectorizer()
    data = cv.fit_transform(
        [c1,c2,c3])
    # print(data)
    print(cv.get_feature_names())
    print(data.toarray())  # 转成数组


def tfidfvec():
    """
    中文字符特征化, 判别分词的重要性
    :return:
    """
    c1, c2, c3 = cutword()
    tf = TfidfVectorizer()
    data = tf.fit_transform([c1,c2,c3])
    print(tf.get_feature_names())
    print(data.toarray())  # 转成数组


if __name__ == '__main__':
    # dictvec()
    # countvec()
    # hanzivec()
    # cutword()
    tfidfvec()
