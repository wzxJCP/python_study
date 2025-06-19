from lxml import etree

# xpath 解析
# （1）本地文件
# （2）服务器响应的数据 response.read().decode('utf-8')
#  本地文件解析
tree = etree.parse("02_xpath的基本使用1.html")
# tree.xpath('xpath路径')
#print(tree)

# 1.路径查询 ”//；/“
# 查找ul下面的li
# li_list = tree.xpath('//body/ul/li')

# 2.谓词查询 “//div[@id]”
# 查找所以有id属性的li标签
# text() 获取标签中的内容
# li_list = tree.xpath('//ul/li[@id]/text()')

# 找到id为l4的li标签 注意引号的问题
# li_list = tree.xpath('//ul/li[@id="l4"]/text()')

# print(li_list)
# print(len(li_list))  # 判断列表的长度

# 3.属性查询 “//@class”
# 查找到id为l4的li标签的class的属性值
# li = tree.xpath('//ul/li[@id="l4"]/@class')
# print(li)
# print(len(li))  # 判断列表的长度

# 4.模糊查询 “//div[contains(@id,"l”)]”
# 查询id中包含l的li标签 【contains（包含）有】
# li_list = tree.xpath('//ul/li[contains(@id,"l")]/text()')

# 查询id的值以c开头的li标签 【starts-with（从……开始）有】
# li_list = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')

# 5.内容查询 “//div/l4/text()“
# 查询 id为l4 和 class为“km”的 （and 双条件）
# li_list = tree.xpath('//ul/li[@id="l4" and @class="km"]/text()')

# 6.逻辑运算
# 查询id为l4和class为km的
# li_list = tree.xpath('//ul/li[@id="l4" and @class="km"]/text()')
li_list = tree.xpath('//ul/li[@id="l4"]/text() | //ul/li[@id="l1"]/text()')

print(li_list)
print(len(li_list))  # 判断列表的长度
