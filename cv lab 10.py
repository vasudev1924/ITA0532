import cv2

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error loading image")
else:
    rotate = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    cv2.imshow("Rotated", rotate)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
