import os
import requests
from bs4 import BeautifulSoup

# 目标URL
url = "https://max.book118.com/html/2022/1108/8020042034005011.shtm"

# 发送GET请求
response = requests.get(url)

# 解析HTML内容
soup = BeautifulSoup(response.text, 'html.parser')

# 查找目标PDF链接
pdf_link = soup.find('//div[@class="webpreview-grab"]')

# 下载PDF文件
filename = os.path.join("downloads")

print(f"PDF file downloaded to: {filename}")