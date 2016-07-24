
import logging
import bs4
import re
import requests

from comm.comm import date_str,  movie_field, movie_url

# 电影解析
from model.video import Video
from parser.teleplay_parser import TeleplayUrlHelper


class MovieParser(object):

    __video_field = movie_field
    __video_url = movie_url
    __video_classify = '电影'
    __video_set = set()

    def __init__(self):
        pass

    def parse_videos(self):
        result_file = 'midRes/' + self.__video_field + '_' + date_str + '.txt'
        with open(result_file, 'a') as to_file:
            self.__parse_videos_into_file(to_file)

    def __parse_videos_into_file(self, to_file):
        all_suffixes = self.__get_all_suffixes()
        if all_suffixes is None:
            return None
        logging.info('all_suffixes共 ' + str(len(all_suffixes)) + ' 条')
        for suffix in all_suffixes:
            logging.info('开始获取 suffix: %s 的所有video', suffix)
            page_index = 1
            while 1:
                page_url = self.__video_url + suffix + str(page_index) + '.html'
                # 获取html页面
                try:
                    response = requests.get(page_url)
                except:
                    logging.warning('获取第 %d 页异常', page_index)
                    logging.exception('exception')
                    continue

                logging.info('#### 开始解析第 %d 页', page_index)

                # 解析html页面
                soup = bs4.BeautifulSoup(response.text, 'html.parser')
                # 获取所有视频标签
                items = soup.find_all('ul', {'p', 'pv'})
                self.__parse_video_list(items, to_file)
                # 没有下一页则终止
                pages_tag = soup.find('ul', 'pages')
                if pages_tag is None or pages_tag.find(class_='next') is None:
                    logging.info('共 %d 页', page_index)
                    break
                logging.info('#### 完成解析第 %d 页', page_index)
                page_index += 1

            logging.info('完成获取 suffix: %s 的所有video', suffix)

    def __parse_video_list(self, video_items_tag, to_file):
        index = 1
        for item_tag in video_items_tag:
            logging.info('开始解析第 %d 个视频', index)
            try:
                video = self.__get_video(item_tag)
                if video is None:
                    continue
            except Exception as e:
                logging.warning("解析第 %d 个视频异常", index)
                logging.exception("exception")
                # 将其从video set中移除
                if video is not None and video.get_name() is not None:
                    self.__video_set.remove(video.get_name())
                continue
            to_file.write(video.to_string())
            to_file.write('\n')
            to_file.flush()
            logging.info('完成解析第 %d 个视频', index)
            index += 1

    def __get_video(self, item_tag):
        root_index = 'http://www.soku.com'
        video = Video()
        video.set_classify_1(self.__video_classify)
        # 获取title标签
        self.__parse_title(video, item_tag)
        logging.info('视频名称: %s', video.get_name())

        if video.get_name in self.__video_set:
            logging.info('视频 %s 已经存在', video.get_name())
            return None
        else:
            self.__video_set.add(video.get_name())

        # 获取评分标签
        self.__parse_score(video, item_tag)
        # 获取播放源
        self.__parse_source_and_link(video, item_tag)
        # 获取缩略图
        self.__parse_picture_url(video, item_tag)

        # 获取详细链接
        detail_link_tag = item_tag.find('li', 'p_link')
        detail_url = root_index + detail_link_tag.a.attrs.get('href')
        detail_html = requests.get(detail_url)
        soup = bs4.BeautifulSoup(detail_html.text, 'html.parser')
        self.__parse_detail(video, soup)
        return video

    def __parse_title(self, video, soup):
        title_tag = soup.find('li', 'p_title')
        name = title_tag.a.text
        video.set_name(name)

    def __parse_score(self, video, soup):
        score_tag = soup.find('li', 'p_rating')
        if score_tag.find('span') != None:
            score_text = score_tag.span.text
            score = int(float(score_text) * 10)
            video.set_score(score)

    def __parse_source_and_link(self, video, soup):
        source_tag = soup.find('div', {'source', 'source_one'})
        sites_tag = source_tag.find_all('span')
        if len(sites_tag) == 0:
            logging.error('sites_tag error, sites_tag: %s', sites_tag)
        if len(sites_tag) == 1:
            video.set_is_unique(1)
        source = ''
        link = ''
        source_num = 0
        for site_tag in sites_tag:
            source += site_tag.attrs.get('name') + '|'
            link += site_tag.a.attrs.get('href') + '|'
            source_num += 1
        video.set_link(link[0: -1])
        video.set_source(source[0: -1])

    def __parse_picture_url(self, video, soup):
        picture_url_tag = soup.find('li', 'p_thumb')
        picture_url = picture_url_tag.img.attrs.get('original')
        video.set_picture_url(picture_url)

    def __parse_detail(self, video, soup):
        detail_tag = soup.find(class_='detail')
        params_tag = detail_tag.find('ul', 'params').select('li')
        classify_2_tag = params_tag[1]
        classify_3_tag = params_tag[3]
        start_time_tag = params_tag[6]
        count_tag = detail_tag.find('ul', 'stats').select('li')
        intro_tag = detail_tag.find(class_='intro')

        self.__parse_classify_2(video, classify_2_tag)
        self.__parse_classify_3(video, classify_3_tag)
        self.__parse_start_time(video, start_time_tag)
        self.__parse_count(video, count_tag)
        if intro_tag is not None:
            self.__parse_intro(video, intro_tag)

    def __parse_classify_2(self, video, soup):
        classify_2 = soup.span.text.replace('/', '|')
        video.set_classify_2(classify_2)

    def __parse_classify_3(self, video, soup):
        classify_3 = soup.span.text.replace('/', '|')
        video.set_classify_3(classify_3)

    def __parse_classify_4(self, video, soup):
        pass

    def __parse_count(self, video, soup):
        if len(soup) >= 2:
            count_text = soup[1].span.text
            video.set_count(int(count_text.replace(',', '')))
        else:
            logging.warning('count_text is not correct, count_tag: %s', soup.text)

    def __parse_intro(self, video, soup):
        if soup is not None and soup.label is not None:
            soup.label.extract()
            video.set_intro(soup.text
                            .replace(' ', '')
                            .replace('\t', '')
                            .replace('\n', '')
                            .replace('\r', '')
                            )

    def __get_all_suffixes(self):
        url_helper = MovieUrlHelper(self.__video_url)
        # 当尝试超过失败次数时，则跳过
        failed_attempt_times = 3
        all_suffixes = []
        while failed_attempt_times > 0:
            try:
                all_suffixes = url_helper.get_all_suffixes()
                break
            except:
                logging.error("获取all suffixes失败")
                logging.exception("exception")
        return all_suffixes

    def __parse_start_time(self, video, soup):
        start_time_text = soup.span.text.replace(' ', '')
        year_pattern = re.compile('([0-9]+)')
        year_month_pattern = re.compile('([0-9]+)-([0-9]+)')
        if year_pattern.match(start_time_text) is not None:
            start_time_text += '-00-00'
        elif year_month_pattern.match(start_time_text) is not None:
            start_time_text += '-00'
        video.set_start_time(start_time_text)

class MovieUrlHelper(TeleplayUrlHelper):

    def __init__(self, video_url):
        TeleplayUrlHelper.__init__(self, video_url)