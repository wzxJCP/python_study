# 1. 安装 requests 和 Beautiful Soup 库。
# pip install requests
# pip install beautifulsoup4

# 2. 打开 QQ 音乐 MV 页面，获取 MV 的 ID。
# https://y.qq.com/n/ryqq/mv/n0041y2al9o

# 3. 使用 requests 库获取 MV 的 JSON 数据。
import requests

mv_id = 'n0041y2al9o'

# url = f'https://u.y.qq.com/cgi-bin/musicu.fcg?data=%7B%22comm%22%3A%7B%22g_tk%22%3A5381%2C%22uin%22%3A%220%22%2C%22format%22%3A%22json%22%2C%22inCharset%22%3A%22utf-8%22%2C%22outCharset%22%3A%22utf-8%22%2C%22notice%22%3A0%2C%22platform%22%3A%22h5%22%2C%22needNewCode%22%3A1%2C%22_%22%3A1567538954763%7D%2C%22mvinfo%22%3A%7B%22module%22%3A%22video.VideoDataServer%22%2C%22method%22%3A%22get_video_info_batch%22%2C%22param%22%3A%7B%22vidlist%22%3A%5B%22{mv_id}%22%5D%2C%22required%22%3A%5B%22vid%22%2C%22type%22%2C%22name%22%2C%22cover_pic%22%2C%22duration%22%2C%22singers%22%2C%22playcnt%22%2C%22pubdate%22%5D%7D%7D%7D'.format(mv_id=mv_id)

url = f'ttps://apd-d907f30171d3a28b00c19befc03e5102.v.smtcdns.com/mv.music.tc.qq.com/AAXSMQNiDFlNQIOAqYSoau4NUFKIMlj8rmtjh5ezOqog/1D1A3A2C53AD5AE150CBB3083A557C32F70699FB05494F415B46CA65F1830ECF6508623EBAA06C509E060108F5DE7A45ZZqqmusic_default/qmmv_0b53oeaaeaaayeangp35yzrvi4iaajyqaasa.f9944.ts{mv_id}'.format(mv_id=mv_id)

response = requests.get(url)

# 4. 解析 JSON 数据，获取 MV 的真实播放地址。
import json
json_data = json.loads(response.text)
play_url = json_data['mvinfo']['data']['sflist'][0]['freeflow_url'][0]

# 5. 下载 MV。
with open(f'{mv_id}.mp4', 'wb') as f:
    f.write(requests.get(play_url).content)

# 爬取 QQ音乐-MV
# https://y.qq.com/n/ryqq/mv/n0018oavrv9
# F12
# Request URL: https://apd-d976ed2484322e2eb5a8372e1e03616d.v.smtcdns.com/mv.music.tc.qq.com/ActT_kM5pn4nIfx3av5W-FQu_ANGjlIdaBBiyW84c0yQ/
# 8C8EE355F358B028EC72390D3FF57304751B73D58E08F26321E113ADD6849049BEA13F6A0AE6D20F24C3D98547ADC91AZZqqmusic_default/qmmv_0b6bxmaayaaawaadulkf7vrfjoyabs5qadca.f9954.ts