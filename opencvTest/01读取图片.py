#导入cv模块
import cv2 as cv

def main():
    #读取图片
    img = cv.imread('img/0LD.png')
    #显示图片
    cv.imshow('TEAM LEBRON-TEAM DURANT', img)
    #等待
    cv.waitKey(0)
    #释放内存
    cv.destroyAllWindows()

if __name__ == '__main__':
    print("照片读取成功！")
    main()