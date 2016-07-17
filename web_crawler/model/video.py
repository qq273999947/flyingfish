class Video(object):
    def __init__(self):
        self.__name = ''  # 视频名称
        self.__classify_1 = ''  # 一级分类
        self.__classify_2 = ''  # 二级分类
        self.__classify_3 = ''  # 三级分类
        self.__classify_4 = ''  # 四级分类
        self.__link = ''  # 视频url
        self.__picture_url = ''  # 缩略图url
        self.__source = ''  # 视频源（土豆、优酷等）
        self.__is_unique = 0  # 是否独播
        self.__count = 0  # 播放次数
        self.__intro = ''  # 视频简介
        self.__start_time = ''  # 放映时间
        self.__update_time = ''  # 更新时间
        self.__score = 0  # 评分
        self.__drama_num = 1  # 剧集数

    def get_name(self):
        return self.__name

    def get_classify_1(self):
        return self.__classify_1

    def get_classify_2(self):
        return self.__classify_2

    def get_classify_3(self):
        return self.__classify_3

    def get_classify_4(self):
        return self.__classify_4

    def get_link(self):
        return self.__link

    def get_picture_url(self):
        return self.__picture_url

    def get_source(self):
        return self.__source

    def is_unique(self):
        return self.__is_unique

    def get_count(self):
        return self.__count

    def get_intro(self):
        return self.__intro

    def get_start_time(self):
        return self.__start_time

    def get_update_time(self):
        return self.__update_time

    def get_score(self):
        return self.__score

    def get_drama_num(self):
        return self.__drama_num

    def set_name(self, name):
        self.__name = name

    def set_classify_1(self, classify_1):
        self.__classify_1 = classify_1

    def set_classify_2(self, classify_2):
        self.__classify_2 = classify_2

    def set_classify_3(self, classify_3):
        self.__classify_3 = classify_3

    def set_classify_4(self, classify_4):
        self.__classify_4 = classify_4

    def set_link(self, link):
        self.__link = link

    def set_picture_url(self, picture_url):
        self.__picture_url = picture_url

    def set_source(self, source):
        self.__source = source

    def set_is_unique(self, is_unique):
        self.__is_unique = is_unique

    def set_count(self, count):
        self.__count = count

    def set_intro(self, intro):
        self.__intro = intro

    def set_start_time(self, start_time):
        self.__start_time = start_time

    def set_update_time(self, update_time):
        self.__update_time = update_time

    def set_score(self, score):
        self.__score = score

    def set_drama_num(self, drama_num):
        self.__drama_num = drama_num

    def to_string(self):
        return (self.get_name() + '\t' +
                self.get_classify_1() + '\t' +
                self.get_classify_2() + '\t' +
                self.get_classify_3() + '\t' +
                self.get_classify_4() + '\t' +
                self.get_link() + '\t' +
                self.get_picture_url() + '\t' +
                self.get_source() + '\t' +
                str(self.is_unique()) + '\t' +
                str(self.get_count()) + '\t' +
                self.get_intro() + '\t' +
                self.get_start_time() + '\t' +
                self.get_update_time() + '\t' +
                str(self.get_score()) + '\t' +
                str(self.get_drama_num()) + '\t')
