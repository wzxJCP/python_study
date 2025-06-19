# import csv
#
# def main():
#     headers = ['学号', '姓名', '分数']
#     rows = [('202001', '张三', '98'),
#             ('202002', '李四', '95'),
#             ('202003', '王五', '92')]
#     with open('score.csv', 'w', encoding='utf8', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(headers)
#         writer.writerows(rows)
# if __name__ == "__main__":
#     main()


# #newline的作用是防止每次插入都有空行
# import csv
# import keyword
#
# with open("test.csv", "a+", newline='') as csvfile:
#         writer = csv.writer(csvfile)
#         #以读的方式打开csv 用csv.reader方式判断是否存在标题。
#         with open("test.csv", "r", newline="") as f:
#             reader = csv.reader(f)
#             if not [row for row in reader]:
#                 writer.writerow(["型号", "分类"])
#                 writer.writerows([[keyword, miaoshu]])
#             else:
#                 writer.writerows([[keyword, miaoshu]])

# csv_file = open('./测试数据2.csv', 'w', encoding='utf-8-sig', newline='')
# fieldnames = ['姓名', '语文', '数学', '英语']
# csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)csv_writer.writeheader()
# zhangsan = {'姓名': '张三', '语文': '90', '数学': '95', '英语': '93'}
# lisi = {'姓名': '李四', '语文': '87', '数学': '100', '英语': '91'}
# wangwu = {'姓名': '王五', '语文': '97', '数学': '91', '英语': '95'}
# csv_writer.writerow(zhangsan)
# csv_writer.writerow(lisi)
# csv_writer.writerow(wangwu)
# csv_file.close()