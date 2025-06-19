#导入cv模块
import cv2 as cv

def main():
    # 读取图片
    img = cv.imread('img/1LX.png')
    # 修改尺寸
    resize_img = cv.resize(img, dsize=(448, 261))
    # 显示原图
    cv.imshow('LX', img)
    # 显示修改后的
    cv.imshow('LXA', resize_img)
    # 打印原图尺寸大小
    print('未修改：', img.shape)
    # 打印修改后的大小
    print('修改后：', resize_img.shape)
    # 等待
    while True:
        if ord('q') == cv.waitKey(0):
            break
    # 释放内存
    cv.destroyAllWindows()

if __name__ == "__main__":
    print("q键退出！")
    main()