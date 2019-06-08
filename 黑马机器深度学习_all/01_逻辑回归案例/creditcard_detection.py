# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/3/26 16:34
# @File_name:creditcard_detection.py
# @IDE:PyCharm

"""
信用卡欺诈检测
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split, KFold, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, recall_score, classification_report
import itertools
from imblearn.over_sampling import SMOTE
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv('data/creditcard.csv')
# print(data.head())  # 输出前五行数据，查看数据的基本属性格式，确定哪些数据需要进行归一化处理，哪些数据需要删除

# 查看类别数据的数量，确定采样方式
count_classes = pd.value_counts(data['Class'], sort=True).sort_index()
count_classes.plot(kind='bar')
plt.title('Fraud class histogram')
plt.xlabel('Class')
plt.ylabel('Frequency')
plt.show()

# 数据标准化，处理数值高的Amount属性，获取新的数据集, 删除无关列
data['normAmount'] = StandardScaler().fit_transform(data['Amount'].reshape(-1, 1))
data = data.drop(['Time', 'Amount'], axis=1)
# print(data.head())

##########################################################
# 对数据进行下采样：按照非正常类的数量随机抽取正常类的样本
# 获取基本数据
x = data.ix[:, data.columns != 'Class']
y = data.ix[:, data.columns == 'Class']

# 获取正常类的索引
normal_indices = data[data.Class == 0].index

# 获取非正常的索引, 和数量
number_records_fraud = len(data[data.Class == 1])
fraud_indices = np.array(data[data.Class == 1].index)

# 根据随机选取非正常的数量的x
random_normal_indices = np.random.choice(normal_indices, number_records_fraud, replace=False)
random_normal_indices = np.array(random_normal_indices)

# 合并下采样索引
under_sample_indices = np.concatenate([fraud_indices, random_normal_indices])

# 获取下采样数据
under_sample_data = data.iloc[under_sample_indices, :]
x_under_sample = under_sample_data.ix[:, under_sample_data.columns != 'Class']
y_under_sample = under_sample_data.ix[:, under_sample_data.columns == 'Class']

# 显示采样率
print('正常类别百分比：', len(under_sample_data[under_sample_data.Class == 0]) / len(under_sample_data))
print('非正常类别百分比：', len(under_sample_data[under_sample_data.Class == 1]) / len(under_sample_data))
print('采样数：', len(under_sample_data))

###################################################
# 交叉验证，进行调参
# Whole dataset
# test_size：测试集数据的比例，random_state=0：对数据进行洗牌
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

print('Number transcations tain dataset:', len(x_train))
print('Number transcations test dataset:', len(x_test))
print('Total number Transsctions:', len(x_test) + len(x_train))

# Undersampled dataset
x_train_undersample, x_test_undersample, y_train_undersample, y_test_undersample = train_test_split(x_under_sample,
                                                                                                    y_under_sample,
                                                                                                    test_size=0.3,
                                                                                                    random_state=0)

print("#" * 50)
print('Number transcations tain dataset:', len(x_train_undersample))
print('Number transcations test dataset:', len(x_test_undersample))
print('Total number Transsctions:', len(x_test_undersample) + len(x_train_undersample))


# Recall = TP/(TP + FN)  回滚评估，二分类中的评估方法
# 定义交叉验证函数,利用交叉验证确正则惩罚项的参数 C
def printing_Kfold_scores(x_train_data, y_train_data):
    # 调用交叉验证函数，验证5次，不进行洗牌
    fold = KFold(len(y_train_data), 5, shuffle=False)

    # 设置惩罚权重
    c_param_range = [0.01, 0.1, 1, 10, 100]

    results_table = pd.DataFrame(index=range(len(c_param_range), 2), columns=['C_parameter', 'Mean recall score'])
    results_table['C_parameter'] = c_param_range

    # the k_fold will give 2 lists: terain_indices = indices[0], test_indices = indices[1]
    j = 0
    for c_param in c_param_range:
        print('-----------------------------------------------')
        print('C_parameter:', c_param)
        print('-----------------------------------------------\n')

        recall_accs = []
        # enumerate:返回一个枚举类型，第一个参数为数字，第二个参数为序列元素
        for iteration, indices in enumerate(fold, start=1):
            # Call the logistic regression model wioth a certain C parameter,惩罚方式选择l1绝对值正则，l2二分之一的权重平方
            lr = LogisticRegression(C=c_param, penalty='l1')

            # Use the training data to fit the model. In this case, we user thre portion of thr fold to tarain the model with indices[0]. We then predict on the portion assigned as the 'test cross validation' witn indices[1]
            lr.fit(x_train_data.iloc[indices[0], :], y_train_data.iloc[indices[0], :].values.ravel())

            # 进行预测
            y_pred_undersample = lr.predict(x_train_data.iloc[indices[1], :].values)

            # Calculate the recall score and append it to a list for recall scores representing the current c_parameter
            recall_acc = recall_score(y_train_data.iloc[indices[1], :].values, y_pred_undersample)
            recall_accs.append(recall_acc)
            print('Iteration', iteration, ':recall score = ', recall_acc)

        # The mean value of those recall scores is the metric we want to save and get hold of.
        results_table.ix[j, 'Mean recall score'] = np.mean(recall_accs)
        j += 1
        print('Mean recall score', np.mean(recall_accs))

    results_table['Mean recall score'] = results_table['Mean recall score'].astype(float)
    best_c = results_table.loc[results_table['Mean recall score'].idxmax()]['C_parameter']

    # Finally, we can check which C parameter is the best amongst the chosen.
    print('*********************************************************************************')
    print('Best model to choose from cross validation is with C parameter = ', best_c)
    print('*********************************************************************************')

    return best_c


best_c = printing_Kfold_scores(x_train_undersample, y_train_undersample)


###########################################################
# 混淆矩阵
def plot_confusion_matrix(cm, classes, title='Confusion matrix', cmap=plt.cm.Blues):
    """
    This function prints ande plots the confusion matrix
    :param cm:
    :param classes:
    :param title:
    :param cmap:
    :return:
    """

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=0)
    plt.yticks(tick_marks, classes)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j], horizontalalignment='center', color='w' if cm[i, j] > thresh else 'b')

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


lr = LogisticRegression(C=best_c, penalty='l1')
lr.fit(x_train_undersample, y_train_undersample.values.ravel())
y_pred_undersample = lr.predict(x_test_undersample.values)

# 计算样本数据的混淆矩阵
cnf_matrix = confusion_matrix(y_test_undersample, y_pred_undersample)
np.set_printoptions(precision=2)

print("Recall metric in the testing dataset: ", cnf_matrix[1, 1] / (cnf_matrix[1, 0] + cnf_matrix[1, 1]))

# Plot non-normalized confusion matrix
class_names = [0, 1]
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, title='Confusion matrix')
plt.show()

#####################################
# 计算所有数据的混淆矩阵
lr = LogisticRegression(C=best_c, penalty='l1')
lr.fit(x_train, y_train.values.ravel())
y_pred_undersample = lr.predict(x_test.values)

# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred_undersample)
np.set_printoptions(precision=2)

print("Recall metric in the testing dataset: ", cnf_matrix[1, 1] / (cnf_matrix[1, 0] + cnf_matrix[1, 1]))

# Plot non-normalized confusion matrix
class_names = [0, 1]
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, title='Confusion matrix')
plt.show()

#############################################
# 对比不同阈值下的混淆矩阵的精度
lr = LogisticRegression(C=best_c, penalty='l1')
lr.fit(x_train_undersample, y_train_undersample.values.ravel())
# predict_proba:预测概率
y_pred_undersample_proba = lr.predict_proba(x_test_undersample.values)
# 阈值
thresholds = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

plt.figure(figsize=(10, 10))

j = 1
for i in thresholds:
    # 设定阈值比较的规则
    y_test_predictions_high_recall = y_pred_undersample_proba[:, 1] > i

    plt.subplot(3, 3, j)
    j += 1

    # Compute confusion matrix
    cnf_matrix = confusion_matrix(y_test_undersample, y_test_predictions_high_recall)
    np.set_printoptions(precision=2)

    print("Recall metric in the testing dataset: ", cnf_matrix[1, 1] / (cnf_matrix[1, 0] + cnf_matrix[1, 1]))

    # Plot non-normalized confusion matrix
    class_names = [0, 1]
    plot_confusion_matrix(cnf_matrix
                          , classes=class_names
                          , title='Threshold >= %s' % i)

#################################################
# 过采样数据进行分析，利用SMOTE算法

credit_cards = pd.read_csv('creditcard.csv')

columns = credit_cards.columns
# The labels are in the last column ('Class'). Simply remove it to obtain features columns
features_columns = columns.delete(len(columns) - 1)

features = credit_cards[features_columns]
labels = credit_cards['Class']
features_train, features_test, labels_train, labels_test = train_test_split(features,
                                                                            labels,
                                                                            test_size=0.2,
                                                                            random_state=0)
oversampler = SMOTE(random_state=0)
os_features, os_labels = oversampler.fit_sample(features_train, labels_train)

os_features = pd.DataFrame(os_features)
os_labels = pd.DataFrame(os_labels)
best_c = printing_Kfold_scores(os_features, os_labels)

# 过采样混淆矩阵
lr = LogisticRegression(C=best_c, penalty='l1')
lr.fit(os_features, os_labels.values.ravel())
y_pred = lr.predict(features_test.values)

# Compute confusion matrix
cnf_matrix = confusion_matrix(labels_test, y_pred)
np.set_printoptions(precision=2)

print("Recall metric in the testing dataset: ", cnf_matrix[1, 1] / (cnf_matrix[1, 0] + cnf_matrix[1, 1]))

# Plot non-normalized confusion matrix
class_names = [0, 1]
plt.figure()
plot_confusion_matrix(cnf_matrix
                      , classes=class_names
                      , title='Confusion matrix')
plt.show()
