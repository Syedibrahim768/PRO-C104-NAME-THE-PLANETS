import cv2
img =cv2.imread("solar-system.jpg")
#puting text
t="sun"
cv2.putText(img,t,(100,120),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))

t="Mercury"
cv2.putText(img,t,(120,180),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))

t="Venus"
cv2.putText(img,t,(180,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))

t="Earth"
cv2.putText(img,t,(280,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))

t="Mars"
cv2.putText(img,t,(380,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))

t="Jupiter"
cv2.putText(img,t,(480,120),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))

t="Saturn"
cv2.putText(img,t,(750,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))

t="Uranus"
cv2.putText(img,t,(950,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))

t="Neptune"
cv2.putText(img,t,(1100,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(0,0,255))


cv2.imshow("orignal",img)
cv2.waitKey(0)