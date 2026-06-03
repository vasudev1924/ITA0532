import cv2

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error loading image")
else:
    big = cv2.resize(img, None, fx=2, fy=2)
    small = cv2.resize(img, None, fx=0.5, fy=0.5)

    cv2.imshow("Big", big)
    cv2.imshow("Small", small)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
