
import logging

from comm.anime_parser import AnimeParser
from comm.comm import  date_str
from comm.teleplay_parser import TeleplayParser

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

if __name__ == '__main__':
    main()
