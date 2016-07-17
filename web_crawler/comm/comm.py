import time

root_url = 'http://www.soku.com'

# 动漫url
anime_field = 'animelist'
anime_url = root_url + '/channel/' + anime_field
# 电影url
movie_field = 'movielist'
movie_url = root_url + '/channel/' + movie_field
# 电视剧url
teleplay_field = 'teleplaylist'
teleplay_url = root_url + '/channel/' + teleplay_field
# 综艺url
variety_field = 'varietylist'
variety_url = root_url + '/channel/' + variety_field

video_field_list = {anime_field, movie_field, teleplay_field, variety_field}
video_url_list = {anime_url, movie_url, teleplay_url, variety_url}

# video_url_dict = {'动漫':anime_url, '电影':movie_url, '电视剧':teleplay_url, '综艺':variety_url}
video_url_dict = {'动漫':anime_url}
video_field_dict = {'动漫':anime_field, '电影':movie_field, '电视剧':teleplay_field, '综艺':variety_field}

date_str = time.strftime('%Y%m%d', time.localtime())