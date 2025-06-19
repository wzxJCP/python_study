# python_study
python_study...

# PythonProject
## 项目介绍

Scrapy 框架   Opencv

Scrapy 框架架构

Scrapy 框架开发学习！

安装各依赖 pip install xlwt

## 项目目录

1、bugTest          爬取                  测试  
2、creepTest       爬取豆瓣电影    测试  
3、gameTest       游戏                  测试  
4、opencvTest    opencv              测试  
5、scrapyTest     scrapy               测试  
6、zSeeAMovieTest   SeeAMovie 和 music   测试

## scrapy 框架

### scrapy 安装

教学地址尚硅谷：https://www.bilibili.com/video/BV1Db4y1m7Ho?spm_id_from=333.788.player.switch&vd_source=60bcf78bf6350bf113eb3fb3d3e56da7&p=91

 (1) pip install scrapy
 (2) pip install twisted
 (3) 报错2 python -m pip install --upgrade pip
 (4) 版本  scrapy version -v
 (5) 最后未解决 需要下载安装Anaconda 

教学https://blog.csdn.net/wq_ocean_/article/details/103889237?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164661244416780265433045%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=164661244416780265433045&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-103889237.pc_search_result_control_group&utm_term=Anaconda&spm=1018.2226.3001.4187

更新scrapy的版本；用 Python 直接调用 pip 模块安装：`python -m pip install --upgrade scrapy`。

  A.scrapy项目的创建以及运行
  1.创建 scrapy 项目:
      终端输入 scrapy startproject 项目名称
  2.项目组成:
   spiders
   _init__.py
   自定义的爬虫文件.py  ---》由我们自己创建，是实现爬虫核心功能的文件
   _init__-py
   items.py          ---》定义数据结构的地方，是一个继承自scrapy. Item的类
   middlewares.py    ---》中间件代理
   pipelines.py      ---》管道文件,里面只有一个类,用于处理下载数据的后续处理 默认是300优先级,值越小优先级越高(1-1000)
   settings.py       ---》配置文件比如:是否遵守robots协议，User-Agent定义等

  cd /D D:\Qy\2022\PycharmProjects\pythonProject
  cd /D C:\Users\Asus\PycharmProjects\pythonProject

'scrapy' 不是内部或外部命令，也不是可运行的程序 或批处理文件。完美解决！！！！：

  https://blog.csdn.net/u012424313/article/details/91403513?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ELandingCtr%7ERate-1.queryctrv4&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ELandingCtr%7ERate-1.queryctrv4&utm_relevant_index=1

  步骤 一、cmd
  pip install scrapy -i https://pypi.douban.com/simple //下载安装 已安装就免安装 直接创建项目
  cd /D C:\Users\Asus\AppData\Local\Programs\Python\Python39\Scripts  //先cmd 再转盘到Scripts
  scrapy startproject scrapy_baidu    //创建项目名
  完成后再去 （C:\Users\Asus\AppData\Local\Programs\Python\Python39\Scripts）里找

  cmd 创建 非内部命令错误  就使用Terminal创建
  cd /D C:\Users\Asus\AppData\Local\Programs\Python\Python39\Scripts\scrapy_baidu\scrapy_baidu\spiders
  scrapy genspider baidu http://www.baidu.com

 Terminal 创建命令
 cd C:\Users\Asus\PycharmProjects\pythonProject\scrapy_baidu\scrapy_baidu\spiders
 scrapy genspider baidu http://www.baidu.com

 1、创建 scrapy 项目:
 跳转到项目目录
 cd C:\Users\Asus\PycharmProjects\pythonProject
      Terminal输入 scrapy startproject （项目名称）   scrapy_58tc_02 创建(scrapy_58tc_02)项目
 跳转到项目目录spiders中  cd scrapy_58tc_02\scrapy_58tc_02\spiders
教学使用：scrapy genspider tc "https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=jianzhi_B"
下同
 scrapy genspider tc https://bj.58.com/sou/?key=%E5%89%8D%E7%AB%AF%E5%BC%80%E5%8F%91&classpolicy=classify_D   
根目录tc.py
 运行测试
 scrapy crawl tc

CrawlSpider方式创建：
scrapy genspider -t crawl read https://www.dushu.com/book/1188.html

### scrapy 项目创建

`scrapy startproject [项目的名字]`

```tex
1.创建爬虫的项目 scrapy startproject [项目的名字]
              注意：项目的名字不允许使用数字开头，也不能包含中文
2.创建爬虫文件
      在spiders文件夹中创建爬虫文件
      cd 项目的名字\项目的名字\spiders
      C:\Users\Asus\PycharmProjects\pythonProject\scrapy_baidu\scrapy_baidu\spiders
   创建爬虫文件
       scrapy genspider [爬虫文件的名字] [要爬取的网页]
       eg：scrapy genspider baidu http://www.baidu.com
       一般情况下不需要添加http协议 因为start_urls的值是根据allowed_domains修改的
       所以添加了http的话 那么start_urls就需要手动去修改
3.运行爬虫代码
     scrapy crawl 爬虫的名字
     eg:
        scrapy crawl baidu
     # 注释，之后就不遵守robots协议 它是一个君子协议 一般情况下我们不需要遵守
     # ROBOTSTXT_OBEY = True
     在settings.py文件中注释掉。
```

### scrapy 项目结构

```tex
1.scrapy项目的结构
   项目名字
      项目名字
         spiders文件夹（存储的爬虫文件）
                 init
                 (tc) 自定义的爬虫文件 核心功能文件  *****************最重要（主文件）
         init
         items   定义数据结构的地方爬取的效据都包含哪些
         middleware  中间件  代理
         pipelines  管道   用来处理下载的数据
         settings  配置文件  robots协议  ua定义等
2. response的属性和方法
   response.text  获取的是响应的字符串
   response.body  获取的是二进制数据
   response.xpath 可以直接使用xpath方法来解析response中的内容
   response.extract() 提取seletor对象的data属性值
   response.extract_first() 提取的seletor列表的第一个数据
```

### 反爬机制（验证码页面）

```python
从你提供的日志来看，你的 Scrapy 爬虫已经运行了，但在爬取过程中遇到了 百度的反爬机制（验证码页面），导致请求被重定向到一个验证页面而不是目标内容页面。

方法一：设置合适的 User-Agent
在 settings.py 中添加：

python
深色版本
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
或者使用中间件随机切换 UA。

方法二：启用 Cookies
确保 COOKIES_ENABLED 是开启的（默认就是开启的）：

python
深色版本
COOKIES_ENABLED = True
方法三：降低请求频率
设置下载延迟：

python
深色版本
DOWNLOAD_DELAY = 3  # 每次请求间隔3秒
避免短时间内大量请求。

方法四：使用代理 IP（可选）
如果你需要大规模抓取百度内容，建议使用高质量的代理池，防止 IP 被封。

方法五：考虑换用其他方式获取数据
百度搜索结果页面本身并不适合直接通过爬虫抓取，因为：

容易触发验证码；
存在法律和协议风险；
不利于长期稳定抓取。

# settings.py 文件中
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
COOKIES_ENABLED = True
DOWNLOAD_DELAY = 3  # 每次请求间隔3秒
```

