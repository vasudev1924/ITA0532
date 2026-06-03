import cv2

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    rot180 = cv2.rotate(img, cv2.ROTATE_180)

    cv2.imshow("180 Rotation", rot180)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
