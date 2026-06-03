import cv2
import numpy as np

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    rows, cols = img.shape[:2]

    pts1 = np.float32([[0,0], [cols,0], [0,rows], [cols,rows]])
    pts2 = np.float32([[50,50], [cols-50,0], [0,rows], [cols,rows-50]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(img, matrix, (cols, rows))

    cv2.imshow("Perspective", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
