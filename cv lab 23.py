import cv2
import numpy as np

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    kernel = np.ones((9,9), np.uint8)

    tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

    cv2.imshow("Top Hat", tophat)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
