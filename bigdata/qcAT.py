# 将你的所有URL粘贴到这里，或者从文件读取
with open("0613_1.txt", "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

# 使用 set 去重，保持顺序可以用 dict.fromkeys()
unique_urls = list(dict.fromkeys(urls))

# 写入去重后的结果到新文件
with open("0613_1-去重后.txt", "w", encoding="utf-8") as f:
    for url in unique_urls:
        f.write(url + "\n")

print(f"原始链接数量: {len(urls)}")
print(f"去重后链接数量: {len(unique_urls)}")