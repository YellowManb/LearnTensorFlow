import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)
X = tf.placeholder("float", [None, 784])
W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))
y = tf.nn.softmax(tf.matmul(X, W) + b)
y_ = tf.placeholder("float", [None,10])
cross_entropy = -tf.reduce_sum(y_*tf.log(y))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)  # 训练目标
init = tf.initialize_all_variables()  # 初始化所有变量
sess = tf.Session()  # 会话控制，tensorflow的操作核心，所有的操作，包括初始化变量，训练，都需要Session().run()
sess.run(init)
for i in range(1000):
  batch_xs, batch_ys = mnist.train.next_batch(100)
  sess.run(train_step, feed_dict={X: batch_xs, y_: batch_ys})  # feed_dict:传播数据的字典
# a=tf.arg_max(y)
correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))  # 求索引是否相等，返回bool型数值
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))  # tf.reduce_mean()求平均，tf.cast()将数值转换为指定数值类型
print(sess.run(accuracy, feed_dict={X: mnist.test.images, y_: mnist.test.labels}))
print('')
