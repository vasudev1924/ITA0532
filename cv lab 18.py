import cv2

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    roi = img[50:200, 50:200]

    img[0:150, 0:150] = roi

    cv2.imshow("ROI Copy-Paste", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
