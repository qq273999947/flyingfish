import logging

from comm.comm import  date_str
from parser.anime_parser import AnimeParser
from parser.movie_parser import MovieParser
from parser.teleplay_parser import TeleplayParser

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    filename='log/video_parser_' + date_str + '.log',
                    filemode='w')

def main():
    # 获取动漫
    anime_parser = AnimeParser()
    anime_parser.parse_videos()

    # 获取电视剧
    teleplay_parser = TeleplayParser()
    teleplay_parser.parse_videos()

    # 获取电影
    movie_parser = MovieParser()
    movie_parser.parse_videos()

if __name__ == '__main__':
    main()
