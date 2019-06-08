
from inference.poems import start_token, end_token
import collections
import numpy as np

"""
数据预处理模块
"""


def process_poems(file_name):
    poems = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            title, content = line.strip().split(':')
            if '_' in content or '(' in content:
                continue
            if len(content) < 5 or len(content) > 80:
                continue
            # 将每首诗打包
            content = start_token + content + end_token
            poems.append(content)

    # 排序，统计词频
    poems = sorted(poems, key=lambda line : len(line))
    all_words = []
    for poem in poems:
        all_words += [word for word in poem]
    counter = collections.Counter(all_words)
    count_paris = sorted(counter.items(), key=lambda x: x[-1])
    words, _ = zip(*count_paris)
    words = words[:len(words)]

    # 字符编码
    word_int_map = dict(zip(words, range(len(words))))
    poems_vector = [list(map(lambda word: word_int_map.get(word, len(words))))]
    return poems_vector, word_int_map, words


def generate_batch(batch_size, poems_vec, word_to_int):
    # 每次取64首诗进行训练
    n_chunk = len(poems_vec) // batch_size
    x_batches = []
    y_batches = []
    for i in range(n_chunk):
        start_index = i * batch_size
        end_index = start_index + batch_size

        batches = poems_vec[start_index:end_index]
        # 找到这个batch的所有poem中最长的poem的长度
        length = max(map(len, batches))
        # 填充一个这么大小的空batch，空的地方放空格对应的index标号
        x_data = np.full((batch_size, length), word_to_int[' '], np.int32)
        for row in range(batch_size):
            # 每一行就是一首诗，在原本的长度上把诗还原上去
            x_data[row, :len(batches[row])] = batches[row]
        y_data = np.copy(x_data)
        # y的话就是x向左边也就是前面移动一个
        y_data[:, :-1] = x_data[:, 1:]
        """
        x_data             y_data
        [6,2,4,6,9]       [2,4,6,9,9]
        [1,4,2,8,5]       [4,2,8,5,5]
        """
        x_batches.append(x_data)
        y_batches.append(y_data)
    return x_batches, y_batches
