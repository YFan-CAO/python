
import cv2 as cv

face_cascade = cv.CascadeClassifier(
    'F:\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')  # 导入识别脸部的分类器
eye_cascade = cv.CascadeClassifier('F:\opencv-master\data\haarcascades\haarcascade_eye.xml')  # 导入识别眼睛的分类器

img = cv.imread('F:\py zuoye\\cvsixteen1.jpg')  # 读取图像
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # 将图像转化为灰度图

faces = face_cascade.detectMultiScale(gray, 1.1, 5)  # 对脸部分类器的大小以及绘制的框图数目进行限定
for (x, y, w, h) in faces:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)  # 对脸部进行矩形框绘制
    roi_gray = gray[y:y + h, x:x + w]  # 建立这个数据的目的是进行眼睛的识别时减小计算量
    roi_color = img[y:y + h, x:x + w]
    eyes = eye_cascade.detectMultiScale(roi_gray)  # 对眼睛分类器进行限定
    for (ex, ey, ew, eh) in eyes:
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 0, 255), 2)  # 对眼睛进行框取
cv.imshow('img', img)
cv.waitKey(0)
cv.destroyAllWindows()