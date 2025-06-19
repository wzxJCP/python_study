# 定义一个 main 函数，作为程序的主要逻辑入口
def main():
    # 从名为 "16州市.txt" 的文本文件中读取所有 URL 数据
    # 使用 with 可以自动关闭文件，更安全；"r"：表示 read 模式，即“只读”。
    with open("0613_1.txt", "r", encoding="utf-8") as f:
        # 按行读取文件内容，去除每行两端空白（如换行符），过滤空行
        # for line in f: 遍历文件对象 f 的每一行。
        # line.strip(): 去除该行开头和结尾的空白字符（比如 \n, \t, 空格等）。
        # if line.strip(): 这是一个过滤条件，只有当这一行去掉空白后不是空字符串时才保留。
        # 整体：创建一个新的列表 urls，其中包含的是文件中所有非空行，且每行已经去除了首尾空白。
        urls = [line.strip() for line in f if line.strip()]

    # 将去重后的结果转换为列表
    # 使用 dict.fromkeys() 去重，并保留原始顺序（因为字典在 Python 3.7+ 中是有序的）
    # 创建一个字典，键来自 unique_urls  列表。如果有多余的重复项，字典会自动去重（因为字典的键必须唯一）。
    unique_urls = list(dict.fromkeys(urls))

    # 将去重后的 URL 写入新文件 "0613_1-去重后.txt"
    with open("0613_1-去重后.txt", "w", encoding="utf-8") as f:
        # 遍历每个去重后的 URL，并写入文件，每个 URL 占一行
        for url in unique_urls:
            f.write(url + "\n")  # 每个 URL 后面加一个换行符

    # 打印处理结果信息到控制台
    print(f"原始链接数量: {len(urls)}")
    print(f"去重后链接数量: {len(unique_urls)}")


# 这是一个常见的 Python 程序结构：
# 如果这个脚本被直接运行（而不是被导入到其他模块中），就执行 main() 函数
if __name__ == "__main__":
    main()