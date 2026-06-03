import cv2
import numpy as np

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    kernel = np.ones((5,5), np.uint8)

    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

    cv2.imshow("Opening", opening)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
