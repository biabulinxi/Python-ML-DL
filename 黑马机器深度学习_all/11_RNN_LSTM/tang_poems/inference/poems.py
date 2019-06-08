import numpy as np
import tensorflow as tf
from models.model import import rnn_model
from dataset.poems import process_poems,generate_batch

# 配置参数
FLAGS = tf.app.flags.FLAGS()
tf.app.flags.DEFINE_integer('batch_size',64,'batch size = ?')
tf.app.flags.DEFINE_float('learning_rate',0.01,'learning rate = ?')
tf.app.flags.DEFINE_string('check_points_dir','./model/','check points dir = ?')
tf.app.flags.DEFINE_string('file_path','./data/.txt','file path = ?')
tf.app.flags.DEFINE_integer('epoch',50,'train epoch')

# 配置写诗的起始标志和终止标志
start_token = 'G'
end_token = 'E'


def run_training():
    # 数据预处理
    poems_vector, word_to_int, vocabularies = process_poems(FLAGS.file_path)
    batch_inputs, batch_outputs = generate_batch(FLAGS.batch_size, poems_vector, word_to_int)
    input_data = tf.placeholder(tf.int32, [FLAGS.batch_size, None])
    output_targets = tf.placeholder(tf.int32, [FLAGS.batch_size, None])

    end_points = rnn_model(model='lstm', input=input_data, output_data=output_targets, vocab_size=len(vocabularies, rnn_size=128, num_layers = 2, batch_size =64, learning_rate=0.01))

def main(is_train):
    if is_train:
        print('traing')
        run_training()
    else:
        print('test')
        begin_word = input('word')


if __name__ == '__main__':
    tf.app.run()