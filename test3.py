import tensorflow as tf
gpu_test = tf.test.is_gpu_available()
print(gpu_test)