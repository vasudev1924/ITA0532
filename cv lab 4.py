import cv2

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("Error loading image")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    equal = cv2.equalizeHist(gray)

    cv2.imshow("Original Gray", gray)
    cv2.imshow("Equalized", equal)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
