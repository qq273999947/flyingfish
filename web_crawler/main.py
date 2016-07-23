import requests
import bs4
import logging
import sys

from comm.UrlHelper import UrlHelper
from comm.comm import video_url_list, video_url_dict, date_str
from comm.video_parser import get_videos

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='log/video_parser_' + date_str + '.log',
                    filemode='w')

for (video_classify, video_url) in video_url_dict.items():
    url_helper = UrlHelper(video_url)
    # 当尝试超过失败次数时，则跳过
    failed_attempt_times = 3
    while failed_attempt_times > 0:
        try:
            all_suffixes = url_helper.get_all_suffixes()
            break
        except:
            logging.error("获取all suffixes失败, video url: %s", video_url)
    if all_suffixes == None:
        continue
    logging.info('all_suffixes共 ' + str(len(all_suffixes)) + ' 条')
    for suffix in all_suffixes:
        logging.info('开始获取 suffix: %s 的所有video', suffix)
        page_index = 1
        while 1:
            page_url = video_url + suffix + str(page_index) + '.html'
            # 获取html页面
            try:
                response = requests.get(page_url)
            except:
                logging.warning('获取第 %d 页异常', page_index)
                continue

            logging.info('#### 开始解析第 %d 页', page_index)

            # 解析html页面
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            # 获取所有视频标签
            items = soup.find_all('ul', {'p', 'pv'})
            get_videos(items, video_classify)
            # 没有下一页则终止
            pages_tag = soup.find('ul', 'pages')
            if pages_tag is None or pages_tag.find(class_='next') is None:
                break
            logging.info('#### 完成解析第 %d 页', page_index)
            page_index += 1

        logging.info('完成获取 suffix: %s 的所有video', suffix)