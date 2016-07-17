import requests
import bs4
import logging
import sys

from comm.comm import video_url_list, video_url_dict, date_str
from comm.video_parser import get_videos

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename= 'log/video_parser_' + date_str + '.log',
                    filemode='w')


for (video_classify, video_url) in video_url_dict.items():
    page_index = 1
    while 1:
        page_url = video_url + '_0_0_0_1_' + str(page_index) + '.html'
        # 获取html页面
        response = requests.get(page_url)

        logging.info('#### 开始解析第 %d 页', page_index)

        # 解析html页面
        soup = bs4.BeautifulSoup(response.text, 'html.parser')
        # 获取所有视频标签
        items = soup.find_all('ul', {'p', 'pv'})
        get_videos(items, video_classify)
        # 没有下一页则终止
        pages_tag = soup.find('ul', 'pages')
        if pages_tag.find(class_='next') is None:
            break

        logging.info('#### 完成解析第 %d 页', page_index)

        page_index += 1

