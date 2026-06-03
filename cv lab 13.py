import cv2
import numpy as np

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    rows, cols = img.shape[:2]

    pts1 = np.float32([[50,50], [200,50], [50,200]])
    pts2 = np.float32([[10,100], [200,50], [100,250]])

    matrix = cv2.getAffineTransform(pts1, pts2)
    result = cv2.warpAffine(img, matrix, (cols, rows))

    cv2.imshow("Affine", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
