def main():
    input_file = "0618_1 - 未去重.txt"
    output_file = "0618_1.txt"

    with open(input_file,"r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    unique_urls = list(dict.fromkeys(urls))

    with open(output_file,"w",encoding="utf-8") as f:
        for url in unique_urls:
            f.write(url + "\n")

    print(f"原始数据量：{len(urls)}")
    print(f"去重数据量：{len(unique_urls)}")

if __name__ == "__main__":
    main()
    print("\n去重完成！")