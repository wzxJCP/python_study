import requests
from pprint import pprint
import pandas as pd

def main():
    url_dict = {
        '全站': 'https://www.bilibili.com/v/popular/rank/all',
        '番剧': 'https://www.bilibili.com/v/popular/rank/bangumi',
        # '国产动画': 'https://www.bilibili.com/v/popular/rank/guochan',
        # '国创相关': 'https://www.bilibili.com/v/popular/rank/guochuang',
        # '纪录片': 'https://www.bilibili.com/v/popular/rank/all',
        # '动画': 'https://www.bilibili.com/v/popular/rank/all',
        # '音乐': 'https://www.bilibili.com/v/popular/rank/all',
        # '舞蹈': 'https://www.bilibili.com/v/popular/rank/all',
        # '游戏': 'https://www.bilibili.com/v/popular/rank/all',
        # '知识': 'https://www.bilibili.com/v/popular/rank/all',
        # '科技': 'https://www.bilibili.com/v/popular/rank/all',
        # '运动': 'https://www.bilibili.com/v/popular/rank/all',
        # '汽车': 'https://www.bilibili.com/v/popular/rank/all',
        # '生活': 'https://www.bilibili.com/v/popular/rank/all',
        # '美食': 'https://www.bilibili.com/v/popular/rank/all',
        # '动物圈': 'https://www.bilibili.com/v/popular/rank/all',
        # '鬼畜': 'https://www.bilibili.com/v/popular/rank/all',
        # '时尚': 'https://www.bilibili.com/v/popular/rank/all',
        # '娱乐': 'https://www.bilibili.com/v/popular/rank/all',
        # '影视': 'https://www.bilibili.com/v/popular/rank/all',
        # '电影': 'https://www.bilibili.com/v/popular/rank/all',
        # '电视剧': 'https://www.bilibili.com/v/popular/rank/all',
        # '原创': 'https://www.bilibili.com/v/popular/rank/all',
        # '新人': 'https://www.bilibili.com/v/popular/rank/all',
    }
    headers = {
        'Accept': 'application, text/plain, */*',  # “接受”:“应用程序、文本/普通
        'Origin': 'https://www.bilibili.com',  # 起点
        'Accept-Encoding': 'br, gzip, deflate',
        'Host': 'https://api.bilibili.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43',
        'Accept-Language': 'zh-cn',
        'Connection': 'keep-alive',
        'Referer': 'https://www.bilibili.com/v/popular/rank/all'
    }
    for i in url_dict.items():
        url = i[1]  # url地址
        tab_name = i[0]  # tab页名称
        title_list = []
        play_cnt_list = []  # 播放数
        danmu_cnt_list = []  # 播放数
        coin_cnt_list = []  # 投币数
        like_cnt_list = []  # 点赞数
        dislike_cnt_list = []  # 点踩数
        share_cnt_list = []  # 分享数
        favorite_cnt_list = []  # 收藏数
        author_list = []
        score_list = []
        video_url = []
        try:
            r = requests.get(url, headers=headers)
            print(r.status_code)
            pprint(r.content.decode())
            pprint(r.json())
            json_data = r.json()
            list_data = json_data['data']['list']
            for data in list_data:
                title_list.append(data['title'])

                play_cnt_list.append(data['stat']['view'])
                danmu_cnt_list.append(data['stat ']['danmaku'])
                coin_cnt_list.append(data['stat ']['coin'])
                like_cnt_list.append(data['stat']['like'])
                dislike_cnt_list.append(data['stat']['dislike'])
                share_cnt_list.append(data['stat']['share'])
                favorite_cnt_list.append(data['stat']['favorite'])
                author_list.append(data['owner']['name'])
                score_list.append(data['score'])
                video_url.append('https://www.bilibili.com/video/' + data['bvid'])

                print('*' * 30)
        except Exception as e:
            print("爬取失败:{}".format(str(e)))

        df = pd.DataFrame(
            {'视频标题': title_list,
             '视频地址': video_url,
             '作者': author_list,
             '综合得分': score_list,
             '播放数': play_cnt_list,
             '弹幕数': danmu_cnt_list,
             '投币数': coin_cnt_list,
             '点赞数': like_cnt_list,
             '点踩数': dislike_cnt_list,
             '分享数': share_cnt_list,
             '收藏数': favorite_cnt_list,
             })
        df.to_csv('B站TOP100-{}.csv '.format(tab_name))
        print('写入成功:' + 'B站TOP100-{}.csv '.format(tab_name))

if __name__ == "__main__":
    main()