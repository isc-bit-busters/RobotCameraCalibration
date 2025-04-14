from picamera2 import Picamera2
import cv2
import time
import os

os.makedirs("calibration_images", exist_ok=True)

picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

i = 0
print("Appuie sur 'c' pour capturer, Échap pour quitter.")

while True:
    frame = picam2.capture_array()
    cv2.imshow("Prévisualisation", frame)

    key = cv2.waitKey(1)
    if key == ord('c'):
        filename = f"calibration_images/image_{i}.jpg"
        cv2.imwrite(filename, frame)
        print(f"Image capturée : {filename}")
        i += 1
    elif key == 27:
        break

cv2.destroyAllWindows()
picam2.stop()
