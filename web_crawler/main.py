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
    pre_index = 2
    while pre_index <= 100:
        page_index = 1

        logging.info('开始解析第 pre %d 页', pre_index)

        while 1:
            page_url = video_url + '_0_0_0_' + str(pre_index) + '_' + str(page_index) + '.html'
            # 获取html页面
            try:
                response = requests.get(page_url)
            except:
                logging.warning('获取第 %d 页异常', page_index)
                continue

            logging.info('#### 开始解析第 %d 页', page_index)

            # 解析html页面
            soup =  bs4.BeautifulSoup(response.text, 'html.parser')
            # 获取所有视频标签
            items = soup.find_all('ul', {'p', 'pv'})
            get_videos(items, video_classify)
            # 没有下一页则终止
            pages_tag = soup.find('ul', 'pages')
            if pages_tag.find(class_='next') is None:
                break
            logging.info('#### 完成解析第 %d 页', page_index)
            page_index += 1

        logging.info('完成解析第 pre %d 页', pre_index)

        pre_index += 1

