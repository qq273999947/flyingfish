
import re
import requests
import logging
import bs4
import time
import traceback

from comm.comm import video_field_dict, date_str
from model.video import Video



def get_videos(items_tag, video_classify):
    video_field = video_field_dict[video_classify]
    to_file = open('midRes/' + video_field + '_' + date_str + '.txt', 'a')
    try:
        index = 1
        for item_tag in items_tag:
            logging.info('开始解析第 %d 个视频', index)
            try:
                video = get_video(item_tag, video_classify)
            except Exception:
                logging.warning("解析第 %d 个视频异常", index)
                return
            video.set_classify_1(video_classify)
            to_file.write(video.to_string())
            to_file.write('\n')

            logging.info('完成解析第 %d 个视频', index)
            index += 1
    finally:
        to_file.close()


def get_video(item_tag, video_classify):
    root_index = 'http://www.soku.com'
    video = Video()
    # 获取title标签
    name_tag = get_name_tag(item_tag, video_classify)
    set_name(video, name_tag)

    logging.info('视频名称: %s', video.get_name())

    # 获取评分标签
    score_tag = get_score_tag(item_tag, video_classify)
    set_score(video, score_tag)
    # 获取播放源
    source_tag = get_source_and_link_tag(item_tag, video_classify)
    set_source_and_link(video, source_tag)
    # 获取缩略图
    picture_url_tag = get_picture_url_tag(item_tag, video_classify)
    set_picture_url(video, picture_url_tag)
    if video_classify == '电视剧' or video_classify == '动漫':
        # 获取剧集标签
        drama_num_tag = get_drama_num_tag(item_tag, video_classify)
        if len(drama_num_tag) > 0:
            set_drama_num(video, drama_num_tag[len(drama_num_tag) - 1])
    # 获取详细链接
    detail_link_tag = item_tag.find('li', 'p_link')
    detail_url = root_index + detail_link_tag.a.attrs.get('href')
    detail_html = requests.get(detail_url)
    soup = bs4.BeautifulSoup(detail_html.text, 'html.parser')
    detail_tag = soup.find(class_ = 'detail')
    set_detail(video, detail_tag, video_classify)
    return video

def get_name_tag(soup, video_classify):
    return soup.find('li', 'p_title')

def get_picture_url_tag(soup, video_classify):
    return soup.find('li', 'p_thumb')

def get_source_and_link_tag(soup, video_classify):
    return soup.find('div', {'source', 'source_one'})

def get_drama_num_tag(soup, video_classify):
    return soup.find('ul', 'linkpanel').find_all('li')

def get_score_tag(soup, video_classify):
    return soup.find('li', 'p_rating')

def set_detail(video, detail_tag, video_classify):
    params_tag = detail_tag.find('ul', 'params').select('li')
    classify_2_tag = params_tag[1]
    classify_3_tag = params_tag[3]
    start_time_tag = params_tag[7]
    count_tag = detail_tag.find('ul', 'stats').select('li')
    intro_tag = detail_tag.find(class_ = 'intro')
    set_classify_2(video, classify_2_tag)
    set_classify_3(video, classify_3_tag)
    set_count(video, count_tag)
    set_start_time(video, start_time_tag)
    set_intro(video, intro_tag)

def set_name(video, title_tag):
    name = title_tag.a.text
    video.set_name(name)

def set_classify_1(video, classify_1_tag):
    pass

def set_classify_2(video, classify_2_tag):
    classify_2 = classify_2_tag.span.text
    video.set_classify_2(classify_2)

def set_classify_3(video, classify_3_tag):
    classify_3 = classify_3_tag.span.text.replace('/', '|')
    video.set_classify_3(classify_3)

def set_classify_4(video, classify_4_tag):
    pass

def set_picture_url(video, picture_url_tag):
    picture_url = picture_url_tag.img.attrs.get('original')
    video.set_picture_url(picture_url)

def set_source_and_link(video, source_tag):
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
    video.set_link(link[0 : -1])
    video.set_source(source[0 : -1])

def set_count(video, count_tag):
    if len(count_tag) >= 2:
        count_text = count_tag[1].span.text
        video.set_count(int(count_text.replace(',', '')))
    else:
        logging.warning('count_text is not correct, count_tag: %s', count_tag.text)

def set_intro(video, intro_tag):
    intro_tag.label.extract()
    video.set_intro(intro_tag.text.replace('\r', '').replace('\n', '').replace('\t', ''))

def set_start_time(video, start_time_tag):
    pass

def set_update_time(video, update_time_tag):
    pass

def set_drama_num(video, drama_num_tag):
    drama_num = int(drama_num_tag.a.text)
    video.set_drama_num(drama_num)

def set_score(video, score_tag):
    if score_tag.find('span') != None:
        score_text = score_tag.span.text
        score = int(float(score_text) * 10)
        video.set_score(score)