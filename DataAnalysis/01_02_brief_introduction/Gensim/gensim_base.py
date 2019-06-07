# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/1/25 10:55
# @File_name:gensim_base.py
# @IDE:PyCharm

import gensim, logging

# logging输出训练日志
logging.basicConfig(format='%(asctime)s : %(levelname)s :'
                           '%(message)s', level=logging.INFO)

# 分好词的句子，每个句子以词列表的形式输入
sentences = [['first', 'sentence'],['second', 'sentence']]

# 用以上句子训练向量模型
model = gensim.models.Word2Vec(sentences, min_count=1)

# 输出单词sentence的词向量
print(model['sentence'])