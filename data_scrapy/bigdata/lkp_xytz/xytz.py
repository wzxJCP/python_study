# 协议投资筛选
import pandas as pd
def main():
    # 指定原始Excel文件的路径
    file_path = '项目沙盘签约项目清单 (2024).xlsx'  # 确保文件在当前工作目录中，或者提供完整路径

    # 读取Excel文件
    df = pd.read_excel(file_path)

    # 筛选“协议投资:万元”列等于或大于10000的数据
    filtered = df[df['协议投资:万元'] >= 10000]

    # 保存筛选后的数据到新的Excel文件
    output_file_path = '协议投资_1亿元以上项目清单（2024）.xlsx'
    filtered.to_excel(output_file_path, index=False)

    print(f"筛选后的数据已保存至：{output_file_path}")

if __name__ == "__main__":
    main()
    print("\n运行完成！")
