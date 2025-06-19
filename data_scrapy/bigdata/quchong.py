# 给定的URL列表
urls = [
    "https://invest.yn.gov.cn/mahj0415ig3dguy60.htm",
    "https://invest.yn.gov.cn/card0415nif/",
    "https://invest.yn.gov.cn/tee0415gkez3i/",
    "https://invest.yn.gov.cn/bmw0415k7o554x.htm",
    "https://invest.yn.gov.cn/mahj0415ig3dguy60.htm", # 重复项
    "https://invest.yn.gov.cn/card0415nif/", # 重复项
    "https://invest.yn.gov.cn/fish04158rtg7ej/",
    "https://invest.yn.gov.cn/tee0415x2e29fit/"
]

# 使用set数据结构去除重复项
unique_urls = list(set(urls))

# 打印去重后的URL列表
for url in unique_urls:
    print(url)