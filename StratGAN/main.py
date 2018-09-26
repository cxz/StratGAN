import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import os

from utils import Config, mkdirs
from model import StratGAN



# Setup configuration
# -----------
config = Config()
# config.image_dir = os.path.join(os.pardir, 'data', 'multi_line')
config.image_dir = os.path.join(os.pardir, 'data', 'fake_single_line')
config.image_ext = '*.png'
config.img_verbose = True
config.c_dim = 1
config.override_mnist = True            # override ALL other dataset parameters and use MNIST

config.batch_size = 100
config.repeat_data = True
config.shuffle_data = True
config.buffer_size = 10
config.drop_remainder = True            # currently fails if false!

config.z_dim = 100                      # number inputs to gener

config.epoch = 10
config.learning_rate = 0.00002           # optim learn rate
config.beta1 = 0.5                      # momentum

config.log_dir = 'log'
config.out_dir = 'out'
config.samp_dir = 'samp'
config.chkp_dir = 'chkp'


# create folder structure
# -----------
mkdirs(config)


# model execution
# -----------
with tf.Session() as sess:
    
    # Initiate session and initialize all vaiables
    stratgan = StratGAN(sess, config)
    
    stratgan.train()
