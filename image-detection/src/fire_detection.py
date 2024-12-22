import cv2
import numpy as np
import pandas as pd
import tensorflow as tf

from tensorflow import keras
from tensorflow.keras import layers,models
from keras_preprocessing.image import ImageDataGenerator

from pathlib import Path

webcam = cv2.VideoCapture(1)





def classify_image():
    image_generator = ImageDataGenerator(
        preprocessing_function=tf.keras.applications.mobilenet_v2.preprocess_input
    )


    model = keras.models.load_model('model/final_model.h5')  # 모델 위치

    filepaths = [Path("")]  # 이미지 위치
    labels = [" "]

    filepaths = pd.Series(filepaths, name='Filepath').astype(str)
    labels = pd.Series(labels, name='Label')

    image_df = pd.concat([filepaths, labels], axis=1)


    input_image = image_generator.flow_from_dataframe(
        dataframe=image_df,
        x_col='Filepath',
        y_col='Label',
        target_size=(224, 224),
        color_mode='rgb',
        class_mode='categorical',
        batch_size=32,
        shuffle=False
    )

    model.predict(input_image)

    np.argmax(model.predict(input_image),axis=1) #산물일때 > array([0], dtype=int64) 아닐때 > array([1], dtype=int64)