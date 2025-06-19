def main():
    input_file = "16州市.txt"
    output_file = "德宏州去重后.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        # 读取所有非空行，并去除两端空白
        urls = [line.strip() for line in f if line.strip()]

    # 使用 dict.fromkeys() 去重，并保持顺序
    unique_urls = list(dict.fromkeys(urls))

    with open(output_file, "w", encoding="utf-8") as f:
        for url in unique_urls:
            f.write(url + "\n")

    # 打印统计信息
    print(f"原始链接数据量：{len(urls)}")
    print(f"去重后链接数据：{len(unique_urls)}")


if __name__ == "__main__":
    main()
    print("\n去重完成！")