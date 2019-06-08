# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/17 9:02
# @File_name:01_yahoo_sz.py
# @IDE:PyCharm

"""
从雅虎财经获取AAPL股票交易数据，对苹果公司股价预测分析
"""

import datetime
import pandas_datareader as pdr
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_pacf, plot_acf
from statsmodels.tsa.arima_model import ARIMA


class AAPLPredict():
    def __init__(self):
        """从雅虎财经获取交易数据"""
        plt.rcParams['font.sans-serif'] = ['SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        start = datetime.datetime(2010,4,1)
        end = datetime.datetime(2019,4,1)
        self.apple = pdr.get_data_yahoo('AAPL',start,end)
        # print(apple.head())

    def resample_plot(self):
        """
        数据重采样, 并进行可视化
        :return: 返回重采样的训练数据
        """
        aapl_week = self.apple['Close'].resample('W-MON').mean()
        aapl_train = aapl_week
        aapl_train.plot(figsize=(12,8))
        plt.legend(bbox_to_anchor=(1.25, 0.5))
        plt.title("Stock Close")
        plt.show()
        return aapl_train

    def diff1(self):
        """进行一阶差分，将非平稳数据平稳化, 并进行可视化"""
        aapl_train = self.resample_plot()
        aapl_diff1 = aapl_train.diff().dropna()
        plt.figure()
        plt.plot(aapl_diff1)
        plt.title('一阶差分')
        plt.show()
        return aapl_diff1

    def diff2(self):
        """进行二阶差分，将非平稳数据平稳化, 并进行可视化"""
        aapl_train = self.diff1()
        aapl_diff2 = aapl_train.diff().dropna()
        plt.figure()
        plt.plot(aapl_diff2)
        plt.title('二阶差分')
        plt.show()
        return aapl_diff2

    def acf_pacf(self):
        """自相关分析和偏自相关分析"""
        acf = plot_acf(self.diff2(), lags=20)
        plt.title('ACF')
        acf.show()
        pacf = plot_pacf(self.diff2(), lags=20)
        plt.title('PACF')
        pacf.show()

    def model(self):
        """建立模型进行训练"""
        aapl_train = self.resample_plot()
        arima = ARIMA(aapl_train, order=(1, 2, 1), freq='W-MON')
        arima = arima.fit()
        # print(model.summary())  # 输出模型报告
        pred = arima.predict('2018-10-01','2019-04-18', dynamic=True, typ='levels')
        print(pred)

        plt.figure()
        plt.xticks(rotation=45)
        plt.plot(pred)
        plt.plot(aapl_train)
        plt.show()


if __name__ == '__main__':
    aapl = AAPLPredict()
    # aapl.resample_plot()
    # aapl.diff1()
    # aapl.diff2()
    # aapl.acf_pacf()
    aapl.model()
