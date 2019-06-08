# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/15 11:33
# @File_name:02_keywordExtraction.py
# @IDE:PyCharm

"""
贝叶斯新闻关键词提取 和 新闻分类
"""

import pandas as pd
import jieba
import jieba.analyse
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from gensim import corpora
import gensim
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB


class KeywordExtraction():
    """
    ---------------贝叶斯新闻关键词提取和分类----------------
    """

    def __init__(self):
        """读取数据"""
        data = pd.read_table('./data/val.txt', names=['category', 'theme', 'URL', 'content'], encoding='utf-8')
        self.data = data.dropna()
        self.stopwords = pd.read_csv("./data/stopwords.txt",index_col=False,sep="\t",quoting=3,names=['stopword'], encoding='utf-8')

    def content(self):
        """
        使用结巴分词器对新闻内容进行分词
        :return: 返回分词好的新闻内容列表
        """
        content = self.data.content.values.tolist()
        content_S = []
        for line in content:
            current_segment = jieba.lcut(line)
            if len(current_segment) > 1 and current_segment is not '\n\r':
                content_S.append(current_segment)
        return content_S

    def drop_stopwords(self):
        """
        从新闻内容中删除掉停用词，留下基本关键词
        :return:  list of list 格式的基本关键词，所有的词统计
        """
        contents = self.content()
        stopwords = self.stopwords.stopword.values.tolist()

        contents_clean = []
        all_words = []
        for line in contents:
            line_clean = []  # 每篇新闻内容的基本关键词
            for word in line:
                if word in stopwords:
                    continue
                line_clean.append(word)
                all_words.append(str(word))
            contents_clean.append(line_clean)
        return contents_clean, all_words

    def word_cloud_plot(self, all_words):
        """
        根据基本关键词，进行词云图绘制
        :return: None
        """
        df_words = pd.DataFrame({'all_words': all_words})  # 转换基本关键词格式
        words_count = df_words.groupby(by=['all_words'])['all_words'].agg({'count': np.size})  # 进行分组聚合
        words_count = words_count.reset_index().sort_values(by=["count"], ascending=False)  # 排序重新设置索引

        matplotlib.rcParams['figure.figsize'] = (10.0, 5.0)
        wordcloud = WordCloud(font_path='./data/simhei.ttf', background_color='white', max_font_size=80)
        word_frequence = {x[0]: x[1] for x in words_count.head(100).values}
        wordcloud = wordcloud.fit_words(word_frequence)
        plt.imshow(wordcloud)
        plt.show()

    def tf_idf(self, contents_clean):
        """
        TF-IDF提取关键词, LDA 主体模型
        :return:
        """
        # gensim 获取全局集合字典
        dic = corpora.Dictionary(contents_clean)
        corpus = [dic.doc2bow(sentence) for sentence in contents_clean]  # 获取语料库
        lda = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=dic, num_topics=20)  # lda 线性判别分析
        topics = []
        for topic in lda.print_topics(num_topics=20,num_words=5):
            topics.append(topic)
        topics = pd.DataFrame({'topics': topics})
        print(topics.head())

    def jieba_analyze(self):
        """
        结巴分词关键词分析
        :return: 文章关键词
        """
        content_S = self.content()
        keywords = []
        for i in range(len(content_S)):
            content_S_str = ''.join(content_S[i])
            keyword = ' '.join(jieba.analyse.extract_tags(content_S_str, topK=5, withWeight=False))
            keywords.append(keyword)

        self.data['keywords'] = keywords
        print(self.data.head())
        # return keywords

    def classify(self, contents_clean):
        """
        新闻分类
        :return:
        """
        df_train = pd.DataFrame({'contents_clean':contents_clean,'label':self.data['category']})
        # 分类数字化
        label_mapping = {"汽车": 1, "财经": 2, "科技": 3, "健康": 4, "体育": 5, "教育": 6, "文化": 7, "军事": 8, "娱乐": 9, "时尚": 0}
        df_train['label'] = df_train['label'].map(label_mapping)  # 映射标签

        # 切分数据
        x_train, x_test, y_train, y_test = train_test_split(df_train['contents_clean'].values, df_train['label'].values,
                                                            test_size=0.25)
        # x_train, content 统计转换向量化
        words = []
        for line_index in range(len(x_train)):
            try:
                words.append(' '.join(x_train[line_index]))
            except:
                continue
        cv = CountVectorizer(analyzer='word', max_features=4000, lowercase=False)
        x_train = cv.fit_transform(words)

        # x_test, content 统计转换向量化
        test_words = []
        for line_index in range(len(x_test)):
            try:
                test_words.append(' '.join(x_test[line_index]))
            except:
                continue
        x_test = cv.transform(test_words)

        # 构建贝叶斯分类器, 利用统计向量转换进行分析
        mlt = MultinomialNB()
        mlt.fit(x_train, y_train)
        print(mlt.score(x_test, y_test))

        # 中文字符特征化, 判别分词的重要性
        tfidf = TfidfVectorizer(analyzer='word', max_features=4000, lowercase=False)
        x_train = tfidf.fit_transform(words)
        x_test = tfidf.transform(test_words)

        # 构建贝叶斯分类器， 利用分词进行分析
        mlt = MultinomialNB()
        mlt.fit(x_train, y_train)
        print(mlt.score(x_test, y_test))


    def workOn(self):
        """ 启动函数"""
        contents_clean, all_words = self.drop_stopwords()
        # self.word_cloud_plot(all_words)
        # self.tf_idf(contents_clean)
        self.classify(contents_clean)


if __name__ == '__main__':
    ke = KeywordExtraction()
    ke.workOn()
    # ke.jieba_analyze()
