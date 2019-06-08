# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/15 9:17
# @File_name:01_correctSpelling.py
# @IDE:PyCharm

import re
import collections as clc

class CorrectSpell():
    """
    --------------------贝叶斯拼写纠正检查--------------------------

    求解：argmaxc P(c|w) -> argmaxc P(w|c) P(c) / P(w)
    P(c), 文章中出现一个正确拼写词 c 的概率, 也就是说, 在英语文章中, c 出现的概率有多大
    P(w|c), 在用户想键入 c 的情况下敲成 w 的概率. 因为这个是代表用户会以多大的概率把 c 敲错成 w
    argmaxc, 用来枚举所有可能的 c 并且选取概率最大的

    """

    def words(self):
        """
        读取语料库的单词，全部转换为小写，同时去除单词中的特殊符号
        :return: 所有转换过的单词
        """
        text = open('./big.txt').read()
        features = re.findall('[a-z]+', text.lower())
        return features

    def count(self):
        """
        统计语料库当中每个单词出现的次数，若没有出现的单词次数记为1，避免概率为0
        :return: 返回处理过的单词统计
        """
        features = self.words()
        Nwords = clc.defaultdict(lambda: 1)
        for f in features:
            Nwords[f] += 1
        return Nwords

    def edits1(self, word):
        """
        编辑距离:两个词之间的编辑距离定义为使用了几次插入(在词中插入一个单字母), 删除(删除一个单字母), 交换(交换相邻两个字母), 替换(把一个字母换成另一个)的操作从一个词变到另一个词.
        :return: 返回所有与单词 w 编辑距离为 1 的集合
        """
        n = len(word)
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        return set([word[0:i] + word[i+1:] for i in range(n)] +                            # 删除距离
                   [word[0:i] + word[i+1] + word[i] + word[i+2:] for i in range(n-1)] +    # 字母顺序调换距离
                   [word[0:i] + c + word[i + 1:] for i in range(n) for c in alphabet] +    # 字母替换距离
                   [word[0:i] + c + word[i:] for i in range(n + 1) for c in alphabet]      # 字母插入距离
                   )

    def edits2(self, word):
        """
        在这些编辑距离小于2的词中间, 只把那些正确的词作为候选词, 在距离为 1 的基础上，在进行距离为 1，循环
        :return: 返回所有与单词 w 编辑距离为 2 的集合
        """
        return set(e2 for e1 in self.edits1(word) for e2 in self.edits1(e1))

    def known(self, words):
        """
        查看输入单词是否在语料库, 判断是否输入正确
        :param words: 输入单词
        :return: 返回存在的单词
        """
        return set(w for w in words if w in self.count())

    def correct(self, word):
        # 如果known(set)非空, candidate 就会选取这个集合, 而不继续计算后面的
        candidates = self.known([word]) or self.known(self.edits1(word)) or self.edits2(word) or [word]
        return print(max(candidates, key=lambda w: self.count()[w]))

if __name__ == '__main__':
    cp = CorrectSpell()
    # words = input('Please input words:')
    cp.correct('appla')
