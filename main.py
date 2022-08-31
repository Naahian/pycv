import cv2

cats = cv2.imread("./asset/cats.jpg")

cats = cv2.line(cats, (0,0), (255, 255), (255,0,0), 5)


cv2.imshow("cats",cats)

cv2.waitKey(0)
cv2.destroyAllWindows()