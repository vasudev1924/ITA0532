import cv2
import numpy as np

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    kernel = np.ones((5,5), np.uint8)

    dilation = cv2.dilate(img, kernel, iterations=1)

    cv2.imshow("Dilation", dilation)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
