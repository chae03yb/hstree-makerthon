import cv2
import keras_preprocessing.image
import numpy as np

from tensorflow import keras
import keras_preprocessing
from PIL import Image


def image_test_fire(image: cv2.typing.MatLike) -> bool:
    model = keras.models.load_model('model/final_model.h5')  # 모델 위치
    model.predict(image)

    return not bool(np.argmax(model.predict(image),axis=1)[0])  # 산불일때 > array([0], dtype=int64), 아닐 때 > array([1], dtype=int64)


webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
webcam.set(cv2.CAP_PROP_FPS, 2)

while cv2.waitKey(500) < 0:
    try:
        ret, frame = webcam.read()
        
        # cv2.imshow("test", frame)
        
        cvt_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(cvt_image)

        im_resized = im_pil.resize((224, 224))
        img_array = keras_preprocessing.image.img_to_array(im_resized)
        image_array_expanded = np.expand_dims(img_array, axis=0)
        
        frame = keras.applications.mobilenet.preprocess_input(image_array_expanded)

        print("fire" if image_test_fire(frame) else "not fire")
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break

webcam.release()
# cv2.destroyAllWindows()