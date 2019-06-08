# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/16 14:57
# @File_name:01_movielines.py
# @IDE:PyCharm

"""
movielines 电影推荐
利用 surprise 库进行推荐
"""

from surprise import KNNBasic, SVD, KNNBaseline
from surprise import Dataset
from surprise import evaluate, print_perf
from surprise import GridSearch
import pandas as pd
import io, os


def knn_basic():
    # 加载数据集，并进行交叉验证迭代
    data = Dataset.load_builtin('ml-100k')
    data.split(n_folds=3)

    # 利用基本的协同过滤算法
    knnb = KNNBasic()

    # 利用基本的协同过滤算法KNNBasic，进行模型评估, 评估标准为 均方根误差rmse, 平均绝对误差mae
    eva = evaluate(knnb, data, measures=['RMSE', 'MAE'])

    # 打印推荐的评估值
    print_perf(eva)


def grid_search():
    # 网格交叉验证进行调参
    # n_epochs - SGD过程的迭代次数。默认是 20。
    # lr_all - 所有参数的学习率。默认是0.007。
    # reg_all - 所有参数的正则化术语。默认是 0.02。
    params = {'n_epochs': [5, 10], 'lr_all': [0.002, 0.005], 'reg_all': [0.4, 0.6]}
    grid_search = GridSearch(SVD, param_grid=params, measures=['RMSE', 'FCP'])

    data = Dataset.load_builtin('ml-100k')
    data.split(n_folds=3)
    eva = grid_search.evaluate(data)
    print(eva)
    # best RMSE score
    print(grid_search.best_score['RMSE'])
    # combination of parameters that gave the best RMSE score
    print(grid_search.best_params['RMSE'])
    # best FCP score
    print(grid_search.best_score['FCP'])
    # combination of parameters that gave the best FCP score
    print(grid_search.best_params['FCP'])

    results = pd.DataFrame.from_dict(grid_search.cv_results)
    print(results)

def knn_baseline():
    def read_item_names():
        """
        获取 电影名称
        :return:
        """
        file_name = ('./ml-100k/u.item')
        rid_to_name = {}
        name_to_rid = {}
        with io.open(file_name, 'r', encoding='ISO-8859-1') as f:
            for line in f:
                line = line.split('|')
                rid_to_name[line[0]] = line[1]
                name_to_rid[line[1]] = line[0]
        return rid_to_name, name_to_rid

    data = Dataset.load_builtin('ml-100k')
    trainset = data.build_full_trainset()
    sim_options = {'name': 'pearson_baseline', 'user_based': False}
    algo = KNNBaseline(sim_options=sim_options)
    algo.fit(trainset)

    rid_to_name, name_to_rid = read_item_names()
    toy_story_raw_id = name_to_rid['Now and Then (1995)']
    toy_story_inner_id = algo.trainset.to_inner_iid(toy_story_raw_id)
    toy_story_neighbors = algo.get_neighbors(toy_story_inner_id, k=10)
    toy_story_neighbors = (algo.trainset.to_raw_iid(inner_id) for inner_id in toy_story_neighbors)
    toy_story_neighbors = (rid_to_name[rid] for rid in toy_story_neighbors)

    print()
    print('The 10 nearest neighbors of Toy Story are:')
    for movie in toy_story_neighbors:
        print(movie)

if __name__ == '__main__':
    # knn_basic()
    # grid_search()
    knn_baseline()
