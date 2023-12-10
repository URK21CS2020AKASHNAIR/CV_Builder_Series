import cv2

image = cv2.imread("tom.jpg")
image1 = cv2.imread("rdj.jpg")
image_gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
image_gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
cv2.imshow("Output",image)
cv2.imshow("Output2",image1)

new_image = image[:100,:100]
B = new_image[:,:,0]
G = new_image[:,:,1]
R = new_image[:,:,2]
print('Blue Channel')
print(B)
print('Green Channel')
print(G)
print('Red Channel')
print(R)

B,G,R = cv2.split(new_image)
image_merged = cv2.merge((B,G,R))


cv2.imshow("Output_gray",image_gray)
cv2.imwrite("gray.jpg",image_gray)
cv2.imshow("Output_gray1",image_gray1)
cv2.imwrite("gray1.jpg",image_gray1)
cv2.waitKey()
cv2.destroyAllWindows()