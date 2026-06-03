import cv2

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    rot270 = cv2.rotate(img, cv2.ROTATE_90_COUNTERCLOCKWISE)

    cv2.imshow("270 Rotation", rot270)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
