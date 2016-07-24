import logging
import threading

from comm.comm import  date_str
from parser.anime_parser import AnimeParser
from parser.movie_parser import MovieParser
from parser.teleplay_parser import TeleplayParser

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    filename='log/video_parser_' + date_str + '.log',
                    filemode='w')

def parse_anime_video():
    # 获取动漫
    anime_parser = AnimeParser()
    anime_parser.parse_videos()

def parse_teleplay_video():
    # 获取电视剧
    teleplay_parser = TeleplayParser()
    teleplay_parser.parse_videos()

def parse_movie_video():
    # 获取电影
    movie_parser = MovieParser()
    movie_parser.parse_videos()

def main():

    anime_parser_thread = threading.Thread(target=parse_anime_video, name="AnimeParser")
    teleplay_parser_thread = threading.Thread(target=parse_teleplay_video, name="TeleplayParser")
    movie_parser_thread = threading.Thread(target=parse_movie_video, name="MovieParser")

    anime_parser_thread.start()
    teleplay_parser_thread.start()
    movie_parser_thread.start()

    anime_parser_thread.join()
    logging.info('AnimeParser thread 执行完毕')
    teleplay_parser_thread.join()
    logging.info('TeleplayParser thread 执行完毕')
    movie_parser_thread.join()
    logging.info('MovieParser thread 执行完毕')

if __name__ == '__main__':
    main()
