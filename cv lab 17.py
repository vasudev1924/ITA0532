import cv2

path = r"C:\Users\akula\OneDrive\Pictures\Desktop\images.webp"
img = cv2.imread(path)

if img is None:
    print("❌ Error")
else:
    watermark = img.copy()

    cv2.putText(watermark, "MY WATERMARK", (50,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

    cv2.imshow("Watermarked", watermark)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
