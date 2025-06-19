from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver.chrome import ChromeDriverManager
import time

def fetch_with_selenium():
    url = "https://www.baidu.com/s?wd=site%3Ainvest.yn.gov.cn%20APP&pn=0"

    # 设置无头模式（可选）
    chrome_options = Options()
    chrome_options.add_argument('--headless')  # 无界面浏览器
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')

    # 启动浏览器
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(url)
        time.sleep(5)  # 等待页面加载完成（可根据需要调整）

        # 打印页面标题，确认是否通过验证
        print("当前页面标题：", driver.title)

        # 提取 mu 属性
        elements = driver.find_elements(By.XPATH, '//div[@mu]')
        links = [el.get_attribute("mu") for el in elements]

        if links:
            print("提取到以下链接：")
            for link in links:
                print(link)
        else:
            print("未找到 mu 属性，请检查页面结构。")

    finally:
        driver.quit()


def main():
    print("=== 百度搜索结果爬虫启动 ===")
    fetch_with_selenium()
    print("=== 爬虫执行结束 ===")


if __name__ == '__main__':
    main()