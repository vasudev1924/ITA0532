import cv2

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"

img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    cv2.imshow("Segmented Image", thresh)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
