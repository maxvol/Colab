import os
print(os.environ['VIRTUAL_ENV'])

# Import mlcompute module to use the optional set_mlc_device API for device selection with ML Compute.
#from tensorflow.python.compiler.mlcompute import mlcompute

# Select CPU device.
# mlcompute.set_mlc_device(device_name='cpu') # Available options are 'cpu', 'gpu', and 'any'.

#%tensorflow_version 2.x
import tensorflow as tf
print(tf.__version__)

print('GPU name: {}'.format(tf.test.gpu_device_name()))

