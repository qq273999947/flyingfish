from inspect import stack

import bs4
import requests
import re


class UrlHelper(object):
    # 要抓取网站url前缀
    __page_prefix = ''
    # 要抓取网站url后缀数组
    __page_suffixes = []

    __default_page_suffix = '_0_0_0_1_1.html'

    __default_page_soup = None

    def __init__(self, page_prefix):
        self.__page_prefix = page_prefix
        response = requests.get(page_prefix + self.__default_page_suffix)
        self.__default_page_soup = bs4.BeautifulSoup(response.text)

    def get_all_suffixes(self):
        category_codes = self.__get_all_category_codes()
        area_codes = self.__get_all_area_codes()
        period_codes = self.__get_all_period_codes()
        suffixes_tmp = [(area_codes[0], category_codes[0], period_codes[0])]
        all_suffixes = []
        while len(suffixes_tmp) != 0:
            suffix_tuple = suffixes_tmp.pop()
            suffix = '_' + suffix_tuple[0] + '_' + suffix_tuple[1] + '_' + suffix_tuple[2] + '_1_'
            video_num = UrlHelper.get_num_of_video(self.__page_prefix + suffix + '1.html')
            if video_num <= 2000:
                all_suffixes.append(suffix)
                continue

            if suffix_tuple[0] == area_codes[0]:
                for area_code in area_codes[1:]:
                    suffixes_tmp.append((area_code, suffix_tuple[1], suffix_tuple[2]))
            elif suffix_tuple[2] == period_codes[0]:
                for period_code in period_codes[1:]:
                    suffixes_tmp.append((suffix_tuple[0], suffix_tuple[1], period_code))
            elif suffix_tuple[1] == category_codes[0]:
                for category_code in category_codes[1:]:
                    suffixes_tmp.append((suffix_tuple[0], category_code, suffix_tuple[2]))
            else:
                all_suffixes.append(suffix)
        return all_suffixes


    def __get_all_category_codes(self):
        category_tags = self.__default_page_soup.find(class_='category').find_all('li')
        pattern = re.compile('_[0-9]+_([0-9]+)_[0-9]+_1_')
        category_codes = []
        for category_tag in category_tags:
            href = category_tag.a.attrs['href']
            res = pattern.search(href).groups()
            category_codes.append(res[0])
        return   category_codes

    def __get_all_area_codes(self):
        area_tags = self.__default_page_soup.find(class_='area').find_all('li')
        pattern = re.compile('_([0-9]+)_[0-9]+_[0-9]+_1_')
        area_codes = []
        for area_tag in area_tags:
            href = area_tag.a.attrs['href']
            res = pattern.search(href).groups()
            area_codes.append(res[0])
        return area_codes

    def __get_all_period_codes(self):
        period_tags = self.__default_page_soup.find(class_={'period'}).find_all('li')
        pattern = re.compile('_[0-9]+_[0-9]+_([0-9]+)_1_')
        period_codes = []
        for period_tag in period_tags:
            href = period_tag.a.attrs['href']
            res = pattern.search(href).groups()
            period_codes.append(res[0])
        return period_codes

    # 获取当前url所有视频个数
    @staticmethod
    def get_num_of_video(video_url):
        response = requests.get(video_url)
        soup = bs4.BeautifulSoup(response.text)
        text = soup.find(class_='catastat').span.text
        pattern = re.compile('([0-9]+)')
        res = pattern.search(text).groups()
        if len(res) < 1:
            raise Exception()
        return int(res[0])

