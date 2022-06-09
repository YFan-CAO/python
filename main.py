from fileinput import filename
import imp
from secrets import choice
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
from turtle import color
import easygui as eg
from numpy import size

Folderpath=" "

def savefile(img):
      global Folderpath
      import cv2 as cv
      import datetime
      print(Folderpath)

      if eg.ccbox(title="提示",msg="是否保存新图片？",choices=('                  是                  ','                   否                '))==True:
            curr_time = datetime.datetime.now()
            timestamp=datetime.datetime.strftime(curr_time,'%Y%m%d%H%M%S')
            print(Folderpath)
            path = str(Folderpath)+'/'+timestamp+'.jpg'     #图片路径
            print(path)
            cv.imwrite(Folderpath+'/'+timestamp+'.jpg',img)  #将图片保存为1.jpg


def tupianrenlianshibie(file):
      import cv2 as cv
      from requests import patch

      face_cascade = cv.CascadeClassifier(
      'E:\QQ\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')  # 导入识别脸部的分类器
      eye_cascade = cv.CascadeClassifier('E:\QQ\opencv-master\data\haarcascades\haarcascade_eye.xml')  # 导入识别眼睛的分类器
      path=''
      path=file
      img = cv.imread(path)  # 读取图像
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
      savefile(img)

def shipingrenlianshibie(file):
      import cv2 as cv
      face_cascade = cv.CascadeClassifier(
            'E:\QQ\opencv-master\data\haarcascades\haarcascade_frontalface_default.xml')  # 导入识别脸部的分类器
      eye_cascade = cv.CascadeClassifier('E:\QQ\opencv-master\data\haarcascades\haarcascade_eye.xml')  # 导入识别眼睛的分类器

      capture = cv.VideoCapture(file)  # 通过 videoCapture() 函数可以进行视频信息的导入
      while (True):
    # 获取一帧
            ret, frame = capture.read()  # 读取成功后 ret 返回为为布尔值True,frame返回读取的一帧图像
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

            faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # 前面图像识别中注释过了
      # 大致已经注释过了
            for (x, y, w, h) in faces:
                  cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
                  roi_gray = gray[y:y + h, x:x + w]
                  roi_color = frame[y:y + h, x:x + w]
                  eyes = eye_cascade.detectMultiScale(roi_gray)
                  for (ex, ey, ew, eh) in eyes:
                        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            frame = cv.resize(frame, dsize=None, fx=0.3, fy=0.3)
            cv.imshow('frame', frame)
            if cv.waitKey(1) == ord('b'):  # 按下‘b’键退出窗口
                  break

def tiaozhenhuidu(file):
      import cv2
      import matplotlib.pyplot as plt
      #读取图像信息
      img0 = cv2.imread(file)
      img1 = cv2.resize(img0, dsize = None, fx = 0.5, fy = 0.5)
      img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
      cv2.imwrite("D:/demo/frc-f6aa4294480ce56a47f81f7af29b4f01.jpeg", img2)   #保存灰度图
      h, w = img1.shape[:2]
      print(h, w)
      cv2.namedWindow("W0")
      cv2.imshow("W0", img1)
      cv2.waitKey(delay = 0)

      #Sobel 算子
      img3 = cv2.Sobel (img2, cv2.CV_64F, 0, 1, ksize=5)
      cv2.namedWindow("W3")
      cv2.imshow("W3", img3)
      cv2.waitKey(delay = 0)
      savefile(img3)
      #Laplacian 算子
      img7 = cv2.Laplacian(img2, cv2.CV_64F)
      cv2.namedWindow("W7")
      cv2.imshow("W7", img7)
      cv2.waitKey(delay = 0)
      savefile(img7)

      #Scharr 算子
      img9 = cv2.Scharr(img2, cv2.CV_64F, 0, 1)
      cv2.namedWindow("W9")
      cv2.imshow("W9", img9)
      cv2.waitKey(delay = 0)
      savefile(img9)

      #canny 算子
      img4 = cv2.Canny(img2, 100, 200)
      cv2.namedWindow("W4")
      cv2.imshow("W4", img4)
      cv2.waitKey(delay = 0)
      savefile(img4)

def tiaozhengtupianyingyin(file):
      import cv2    # 调用opencv包
      import numpy as np
      
      img0 = cv2.imread(file)       #读取图像位置
      img1 = cv2.resize(img0, dsize = None, fx = 0.5, fy = 0.5)      #将显示的图像宽和高都变为一半
      img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)     #对图像进行灰度处理
      h, w = img1.shape[:2]
      print(h, w)

      cv2.namedWindow("W0")        #命名一个窗口
      cv2.imshow("W0", img1)       #显示图片
      cv2.waitKey(delay = 0)       #无限期等待下一个命令

      cv2.namedWindow("W1")
      cv2.imshow("W1", img2)
      cv2.waitKey(delay = 0)
      savefile(img2)

      #图像二值化
      ret, img3 = cv2.threshold(img2, 135, 255, cv2.THRESH_BINARY)
      cv2.namedWindow("W2")
      cv2.imshow("W2", img3)
      savefile(img3)

      k = np.ones((5, 5), np.uint8) #创建内核
      #腐蚀
      img4 = cv2.erode(img3, k, iterations = 1)
      cv2.namedWindow("W3")
      cv2.imshow("W3", img4)
      cv2.waitKey(delay = 0)
      savefile(img4)

def youhuaa(file):
      import cv2
      import numpy as np
      import matplotlib.pyplot as plt
      img = cv2.imread(file)
      img = cv2.resize(img, dsize = None, fx = 0.2, fy = 0.2) #由于该算法计算量较大，首先对其大小进行调整
      cv2.imshow('W0', img)
      cv2.waitKey(0)
#获取图片宽高
      height, width = img.shape[:2]
#print(height, width)
      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#将图像转化为灰度图像
      dst = np.zeros((height, width, 3), np.uint8)#创建一个和原图等大小的全零矩阵
#-----------------------------------------------------------------------
#使用for循环嵌套来遍历图像中的每一个像素点
#-----------------------------------------------------------------------
      for i in range(2, height-2):
            for j in range(2, width-2):
      # ----------------------------------------------------------
      # 方框为4*4，对方框内像素点进行量化并记录不同等级的像素点的个数
      # ------------------------------------------------------------
                  array1 = np.zeros(8, np.uint8)#将像素点的值量化为8份，定义数组记录不同等级像素点的个数
                  for m in range(-2, 2):
                        for n in range(-2, 2):
                              p1 = int(gray[i+m, j+n]/32)#量化操作
                              array1[p1] = array1[p1] + 1#该数组用来记录不同量化级别下的像素点，比如array1[0]代表等级一下的像素点的个数，即像素值为（0~64）的像素点的个数
      #-----------------------------------------------------------
      #在上面的数组中寻找最大值，即寻找数目最多的像素等级
      #------------------------------------------------------------
                  currentMax = array1[0]
                  l = 0#用来封装最大值在数组中的位置
                  for k in range(0, 8):
                        if currentMax < array1[k]:
                              currentMax = array1[k]
                              l = k
      #------------------------
      #求数目最多的像素等级的平均
      #------------------------
                  for m in range(-2, 2):
                        for n in range(-2, 2):
                              if gray[i + m, j + n] >= (l * 32) and gray[i + m, j + n] <= ((l + 1) * 32):
                                    (b, g, r) = img[i + m, j + n]
                  dst[i, j] = (b, g, r)
      cv2.imshow('youhua', dst)
      cv2.waitKey(0)
      savefile(dst)

def lvjintexiao(file):
      import cv2
      import numpy as np
      import math
      import matplotlib.pyplot as plt
      
      img0 = cv2.imread(file)
      img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
      h, w = img0.shape[:2]
      cv2.imshow("W0", img0)
      cv2.waitKey(delay = 0)
      #毛玻璃特效
      img2 = np.zeros((h - 6, w - 6, 3), np.uint8)        #生成的全零矩阵考虑到了随机数范围，变小了
      for i in range(0, h - 6):                   #防止下面的随机数超出边缘
            for j in range(0, w - 6):
                  index = int(np.random.random()*6)   #0~6的随机数
                  (b, g, r) = img0[i + index, j + index]
                  img2[i, j] = (b, g, r)
      cv2.imshow("W2", img2)
      cv2.waitKey(delay = 0)
      savefile(img2)

def fugulvjing(file):
      import cv2
      import matplotlib.pyplot as plt
            
      #读取图像信息
      img0 = cv2.imread(file)
      cv2.namedWindow("W0")
      cv2.imshow("W0", img0)
      cv2.waitKey(delay = 0)
      img1 = cv2.resize(img0, dsize = None, fx = 0.6, fy = 0.6)
      img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
      h, w = img1.shape[:2]
      print(h, w)
      cv2.namedWindow("W1")
      cv2.imshow("W1", img2)
      cv2.waitKey(delay = 0)
      savefile(img2)
      #直方图均衡化
      img3 = cv2.equalizeHist(img2)
      cv2.namedWindow("W2")
      cv2.imshow("W2", img3)
      cv2.waitKey(delay = 0)
      savefile(img3)

def huofubianhuan(file):
      import cv2
      import matplotlib.pyplot as plt
      import numpy as np
      
      img0 = cv2.imread(file)
      #img0 = cv2.resize(img0, dsize = None, fx = 0.5, fy = 0.5)
      img1 = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
      h, w = img0.shape[:2]

      cv2.waitKey(delay = 0)
      #霍夫直线检测
      ##首先进行边缘检测，来减少空间中其他的点带来的计算量的问题
      img2 = cv2.GaussianBlur(img1, (5, 5), 0)   #高斯模糊为边缘检测做准备
      img3 = cv2.Canny(img2, 50, 120)            #使用Canny算子进行边缘检测
      cv2.waitKey(delay = 0)
      rho = 1                    #距离分辨率
      theta = np.pi/180          #角度分辨率
      threshold = 10             #霍夫空间中多少个曲线相交表示一个正式的交点
      min_line_len = 50          #最少需要多少个像素点才构成一条直线
      max_line_gap = 50          #线段之间的最大间隔像素点数
      lines = cv2.HoughLinesP(img3, rho, theta, threshold, maxLineGap = max_line_gap)    #所以这个函数中的参数都已经在前面赋值时解释过了
      img4 = np.zeros_like(img3)
      for line in lines:
            for x1, y1, x2, y2 in line:
                  cv2.line(img4, (x1, y1), (x2, y2), 255, 1)        #绘制直线
      cv2.waitKey(delay = 0)
      #霍夫圆检测
      dp = 1              #检测内测圆心的累加器图像的分辨率与输入图像之比的倒数
      minDist = 700       #两个圆之间圆心之间的最小距离
      param1 = 100        #前面提到过 Canny 边缘检测，这个参数表示传递给边缘检测的高阈值
      param2 = 80         #检测阶段圆心的累加器阈值，简单来说该参数越大检测到的圆越完美，但数目越少，反之亦然
      minRadius = 10      #最小圆的半径
      maxRadius = 20      #最大圆的半径
      cirlces = cv2.HoughCircles(img2, cv2.HOUGH_GRADIENT, dp, minDist, param1, param2, minRadius, maxRadius)  #函数的参数前面解释过了
      cirlces = np.uint16(np.around(cirlces))
      img5 = img0
      for i in cirlces[0, :]:
            cv2.circle(img5, (i[0], i[1]), i[2], (0, 0, 255), 1)
            cv2.circle(img5, (i[0], i[1]), 2, (0, 0, 255), 1)
      cv2.waitKey(delay = 0)
      #将所有图像绘制在一张图纸上
      img0 = cv2.imread(file)   #再次读取原图，前面的图像已经进行了变换
      plt.rcParams['font.family'] = 'SimHei'       #将全局中文字体改为黑体
      imgs = [img0, img1, img2, img3, img4, img5]
      title = ['原图', '灰度图', '高斯模糊', '边缘检测', '霍夫直线检测', '霍夫圆检测']
      for i in range(6):
            imgs[i] = cv2.cvtColor(imgs[i], cv2.COLOR_BGR2RGB)
            plt.subplot(2, 3, i + 1)
            plt.imshow(imgs[i])
            plt.title(title[i])
            plt.xticks([])
            plt.yticks([])
      plt.show()
      

def Mysel(filename):
      dic = {0:'图片人脸识别',1:'乙',2:'丙',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8'}
      s = "您选了" + dic.get(var.get()) + "项"
      if var.get()==0:
            tupianrenlianshibie(filename)
      if var.get()==1:
            shipingrenlianshibie(filename)
      if var.get()==2:
            tiaozhenhuidu(filename)
      if var.get()==3:
            tiaozhengtupianyingyin(filename)
      if var.get()==4:
            youhuaa(filename)
      if var.get()==5:
            lvjintexiao(filename)
      if var.get()==6:
            fugulvjing(filename)
      if var.get()==7:
            huofubianhuan(filename)

root = Tk()
root.geometry('860x640')
root.title('图片处理器')

def run1():
      global Folderpath 
      from tkinter import filedialog
      Folderpath = filedialog.askdirectory() #获得选择好的文件夹
      print(Folderpath)




def fileopen():
      file_name =askopenfilename()

      if file_name:
            Mysel(file_name)
      

# 在窗体垂直自上而下位置60%处起，布局相对窗体高度40%高的文本框
lb = Label(root)
var = IntVar()
from PIL import Image, ImageTk
image_file = Image.open("demo.jpg") 
import tkinter
photo = ImageTk.PhotoImage(image_file)
tkinter.Label(root,image=photo).grid(row = 0, column = 0,rowspan=3,columnspan=3)
rd1 = Radiobutton(root,text="图片人脸识别",variable=var,value=0,command=Mysel,font=('黑体', '13'))
rd1.place(x=60,y=40)


rd2 = Radiobutton(root,text="视频人脸识别",variable=var,value=1,command=Mysel,font=('黑体', '13'))
rd2.place(x=260,y=40)


rd3 = Radiobutton(root,text="调整图片灰度",variable=var,value=2,command=Mysel,font=('黑体', '13'))
rd3.place(x=460,y=40)


rd4 = Radiobutton(root,text="调整图片阴影",variable=var,value=3,command=Mysel,font=('黑体', '13'))
rd4.place(x=660,y=40)


rd5 = Radiobutton(root,text="油画特效",variable=var,value=4,command=Mysel,font=('黑体', '13'))
rd5.place(x=60,y=160)


rd6 = Radiobutton(root,text="毛玻璃滤镜特效",variable=var,value=5,command=Mysel,font=('黑体', '13'))
rd6.place(x=260,y=160)


rd7 = Radiobutton(root,text="复古滤镜特效",variable=var,value=6,command=Mysel,font=('黑体', '13'))
rd7.place(x=460,y=160)



rd8 = Radiobutton(root,text="霍夫变换",variable=var,value=7,command=Mysel,font=('黑体', '13'))
rd8.place(x=660,y=160)

btn1 = Button(root, text='选择图片', command=fileopen,font=('Helvetica', '20'),fg="#5E2612")
btn1.place(x=190,y=300,height=120,width=400)

btn2 = Button(root, text='选择图片存储空间', command=run1,font=('Helvetica', '20'),fg = "#9933FA",)
btn2.place(x=190,y=460,height=120,width=400)




root.mainloop()
