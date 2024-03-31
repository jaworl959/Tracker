import cv2
def mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(" x:", x, ", y:", y)
        pixel_value = img[y, x]
        print(" RGB:", pixel_value)
img = cv2.imread('C:/Users/user/Downloads/opalMap.png')
cv2.imshow('image', img)
cv2.setMouseCallback('image', mouse_click)
cv2.waitKey(0)
cv2.destroyAllWindows()
##location aks mored nazar ro midim behesh roye rangi ke rgb ro mikhaim clik mikonim rgb mide