#导入cv模块
import cv2 as cv

def main():
    # 读取图片
    img = cv.imread('img/0LD.png')
    # 灰度转换
    gray_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # 显示灰度图片
    cv.imshow('TEAM LEBRON-TEAM DURANT A', gray_img)
    # 保存灰度图片
    cv.imwrite('img/0LD1.png', gray_img)
    # 显示图片
    cv.imshow('TEAM LEBRON-TEAM DURANT', img)
    # 等待
    cv.waitKey(0)
    # 释放内存
    cv.destroyAllWindows()

if __name__ == "__main__":
    print("灰度转换成功！")
    main()