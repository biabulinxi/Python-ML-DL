# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/17 14:17
# @File_name:01_data_exploration.py
# @IDE:PyCharm

"""
保险数据赔偿预测，数据探索分析
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error
import seaborn as sns
import xgboost as xgb


class MyXgboost():
    """在这一部分，我们做一个简短的数据探索，看看我们有什么样的数据集，以及我们是否能找到其中的任何模式"""

    def __init__(self):
        """获取数据"""
        self.train = pd.read_csv('./data/train.csv')
        self.test = pd.read_csv('./data/test.csv')

    def pre_process(self):
        """数据预处理"""
        # loss 数据对数化
        self.train['log_loss'] = np.log(self.train['loss'])
        # 数据分成连续和离散值
        features = [x for x in self.train.columns if x not in ['id', 'loss', 'log_loss']]
        cat_features = [x for x in self.train.select_dtypes(include=['object']).columns if x not in ['id', 'loss', 'log_loss']]
        con_features = [x for x in self.train.select_dtypes(exclude=['object']).columns if x not in ['id', 'loss', 'log_loss']]
        # 标签编码
        ntrain = self.train.shape[0]
        x_train = self.train[features]
        y_train = self.train['log_loss']

        for cat in range(len(cat_features)):
            x_train[cat_features[cat]] = x_train[cat_features[cat]].astype('category').cat.codes

        return x_train, y_train

    def xg_eval_mae(self, yhat, dtrain):
        """评估函数"""
        y = dtrain.get_label()
        return 'mae', mean_absolute_error(np.exp(y), np.exp(yhat))

    def model(self):
        """
        首先，我们训练一个基本的xgboost模型，然后进行参数调节通过交叉验证来观察结果的变换，
        使用平均绝对误差来衡量mean_absolute_error(np.exp(y), np.exp(yhat))。
        xgboost 自定义了一个数据矩阵类 DMatrix，会在训练开始时进行一遍预处理，从而提高之后每次迭代的效率
        """
        x_train, y_train = self.pre_process()
        dtrain = xgb.DMatrix(x_train, y_train)
        # 参数
        xgb_params = {
            'seed': 0,
            'eta': 0.1,
            'colsample_bytree': 0.5,
            'silent': 1,
            'subsample': 0.5,
            'objective': 'reg:linear',
            'max_depth': 5,
            'min_child_weight': 3
        }
        # 交叉验证
        bst_cv1 = xgb.cv(xgb_params, dtrain, num_boost_round=50, nfold=3, seed=0,feval=self.xg_eval_mae, maximize=False, early_stopping_rounds=10)
        print('CV score:', bst_cv1.iloc[-1, :]['test-mae-mean'])

        # 绘制图形
        plt.figure()
        bst_cv1[['train-mae-mean', 'test-mae-mean']].plot()
        plt.show()


if __name__ == '__main__':
    xgb1 =MyXgboost()
    xgb1.model()
