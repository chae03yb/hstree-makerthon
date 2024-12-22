import cv2
import keras_preprocessing.image
import numpy as np

from tensorflow import keras
import keras_preprocessing
from PIL import Image

import alarm


fire_detect_count = 0
alarm_sent = False
DEVICE_ID = 1


def image_test_fire(image: cv2.typing.MatLike) -> bool:
    model = keras.models.load_model('model/final_model.h5')
    model.predict(image)

    return not bool(np.argmax(model.predict(image),axis=1)[0]) 


webcam = cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
webcam.set(cv2.CAP_PROP_FPS, 2)

while cv2.waitKey(50) < 0:
    try:
        ret, frame = webcam.read()
        
        # cv2.imshow("test", frame)
        
        cvt_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        im_pil = Image.fromarray(cvt_image)

        im_resized = im_pil.resize((224, 224))
        img_array = keras_preprocessing.image.img_to_array(im_resized)
        image_array_expanded = np.expand_dims(img_array, axis=0)
        
        frame = keras.applications.mobilenet.preprocess_input(image_array_expanded)


        print(f"[DEBUG]: count: {fire_detect_count}")
        
        if image_test_fire(frame):
            fire_detect_count += 1
            if fire_detect_count >= 3 and not alarm_sent:
                alarm.send_alarm(DEVICE_ID)
                alarm_sent = True
        else:
            fire_detect_count = 0
            if alarm_sent:
                alarm.suppress_alarm(DEVICE_ID)
                alarm_sent = False
        
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        break

webcam.release()
# cv2.destroyAllWindows()