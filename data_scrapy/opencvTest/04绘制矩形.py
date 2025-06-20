#导入cv模块
import cv2 as cv

def main():
    # 读取图片
    img = cv.imread('img/2LX.png')
    # 坐标
    x, y, w, h = 100, 100, 100, 100
    # 绘制矩形
    cv.rectangle(img, (x, y, x + w, y + h), color=(0, 0, 255), thickness=1)
    # 绘制圆形
    cv.circle(img, center=(x + w, y + h), radius=100, color=(255, 0, 0), thickness=5)
    # 显示
    cv.imshow('LX', img)
    while True:
        if ord('q') == cv.waitKey(0):
            break
    # 释放内存
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
