import cv2

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"

img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    lower = (0, 0, 100)
    upper = (180, 255, 255)

    mask = cv2.inRange(hsv, lower, upper)

    foreground = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("Foreground Extraction", foreground)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
