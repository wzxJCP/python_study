#导入cv模块
import cv2 as cv

def main():
    # 检测函数
    def face_detect_demo():
        gary = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        face_detect = cv.CascadeClassifier('D:\Rj\opencv\sources\data\haarcascades/haarcascade_frontalface_default.xml')
        face = face_detect.detectMultiScale(gary, 1.01, 5, 0, (100, 100), (300, 300))
        for x, y, w, h in face:
            cv.rectangle(img, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        cv.imshow('result', img)

    # 读取图像
    img = cv.imread('img/1LX.png')
    # 检测函数
    face_detect_demo()
    # 等待
    while True:
        if ord('q') == cv.waitKey(0):
            break
    # 释放内存
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()