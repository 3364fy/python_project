# -*- coding:utf-8 -*-
import sys
# sys.setdefaultencoding('utf-8')
import numpy as np
from tensorflow.keras.callbacks import ReduceLROnPlateau,ModelCheckpoint
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import tensorflow as tf
from PIL import Image
import numpy as np
import itertools
import os




im_height = 224#512
im_width = 224#512
batch_size = 1
epochs = 200
#图像存放路径
test_dir = "valid"
test_image_generator = ImageDataGenerator(rescale=1./255)
#路径下两个文件夹,代表两类
test_data_gen = test_image_generator.flow_from_directory(directory=test_dir,
                                                         batch_size=batch_size,
                                                         shuffle=False,
                                                         target_size=(im_height, im_width),
                                                         class_mode='sparse')

total_test = test_data_gen.n
#第一次运行需要花点时间自动下载
covn_base = tf.keras.applications.DenseNet121(weights='imagenet', include_top=False,input_shape=(im_height,im_width,3),pooling='avg')
covn_base.trainable = False
#批量对图像识别
def predict(data,model):
	count=0
	for s in data:
		count+=1
		#图像和真实类别
		img,label=s
		#对单张图片进行识别
		pred_y=model.predict(img)[0].tolist()
		label=label.tolist()
		result =""
		if pred_y[0]>0.9: # 计算之后的概率大于90%
			result='有肿瘤'
		else:
			result = '没有肿瘤'
		print(count,pred_y,result)
		if count>=data.n:
			break
#加载模型
model=tf.keras.models.load_model("model.h5")
predict(test_data_gen,model)

