drop database if exists `flyingfish`;
create database if not exists `flyingfish`;

drop table if exists `video`;
create table `video` (
    `id`            int unsigned    not null    auto_increment  comment '自增主键',
    `name`          varchar(50)     not null    default ''      comment '视频名称',
    `classify_1`    varchar(30)     not null    default ''      comment '一级分类',
    `classify_2`    varchar(30)     not null    default ''      comment '二级分类',
    `classify_3`    varchar(30)     not null    default ''      comment '三级分类',
    `classify_4`    varchar(30)     not null    default ''      comment '四级分类',
    `link`          varchar(500)     not null    default ''      comment '视频链接',
    `picture_url`   varchar(200)     not null    default ''      comment '缩略图地址',
    `source`        varchar(50)    not null    default ''      comment '视频源',
    `is_unique`     tinyint         not null    default 0       comment '是否独播',
    `count`         int             not null    default 0       comment '播放量',
    `intro`         varchar(500)    not null    default ''      comment '简介',
    `start_time`    datetime        not null    default '1970-01-01 00:00:00'   comment '上映时间',
    `update_time`   datetime        not null    default '1970-01-01 00:00:00'   comment '更新时间',
    `score`         tinyint         not null    default 0       comment '评分',
    `drama_num`     tinyint         not null    default 1       comment '剧集数',
    primary key (`id`),
    unique  key (`name`)
) comment '视频信息表' default charset=utf8mb4;


insert into `video`(`name`, `classify_1`, `classify_2`, `classify_3`, `classify_4`, `link`, `picture_url`, `source`, `is_unique`, `count`, `intro`, `start_time`, `update_time`, `score`, `drama_num`) values
('好先生', '电视据', '大陆', '', '', ' http://v.youku.com/v_show/id_XMTU5MDk5MjI4NA==.html|http://www.mgtv.com/v/2/159041/f/3204693.html', 'http://g2.ykimg.com/05160000574E48C167BC3C368802FB10', '优酷|芒果', 0, 2036789335, 'XXX', '2015-00-00', '', 98, 33),
('仙剑云之凡', '电视据', '大陆', '', '', 'http://v.youku.com/v_show/id_XMTU4MTY4OTg5Mg==.html|http://www.tudou.com/albumplay/uQs_5iCkh7Y/fZimC34CYyI.html', 'http://g2.ykimg.com/051600005743DBBB67BC3C23560CBC74', '优酷|土豆', 0, 1201773380, 'XXX', '2015-7-10', '', 94, 20),
('亲爱的翻译官', '电视据', '大陆', '', '', 'http://www.mgtv.com/v/2/151068/f/3181384.html', 'http://g2.ykimg.com/05160000575D297167BC3C0BEA00D402', '芒果', 1, 1887088, 'XXX', '2015-12-21', '', 86, 46),
('余罪', '电视据', '大陆', '', '', 'http://www.iqiyi.com/v_19rrldre6k.html', 'http://g1.ykimg.com/051600005756269767BC3C2D0A03B2EA', '爱奇异', 1, 639186, 'XXX', '2016-00-00', '', 83, 2),
('奶酪陷阱', '电视据', '韩国', '', '', 'http://v.youku.com/v_show/id_XMTU3Mzc4NDA1Mg==.html|http://www.tudou.com/albumplay/1moGApl9O2c/axC0faC3BtY.html', 'http://g3.ykimg.com/05160000573D3DD267BC3C1F80064142', '优酷|土豆', 0, 91065205, 'XXX', '2016-01-04', '', 98, 16),
('太阳的后裔', '电视据', '韩国', '', '', 'http://www.iqiyi.com/v_19rrkxmiss.html', 'http://g3.ykimg.com/0516000056D8FE4867BC3C16270D6DEE', '爱奇异', 1, 7736550, 'XXX', '2016-02-24', '', 91, 16),
('越狱', '电视据', '美国', '', '', 'http://tv.sohu.com/20130914/n386592043.shtml?txid=8254069965286abe9ee523a73c256ea7', 'http://g1.ykimg.com/0516000051E627126758395D8E01056A', '搜狐', 1, 13517707, 'XXX', '2008-09-1', '', 93, 22),
('北京遇上西雅图之不二情书', '电影', '大陆', '爱情', '', 'http://v.youku.com/v_show/id_XMTYxMDkwNzczMg==.html|http://www.tudou.com/albumplay/_IrICiU2Xuo/hJldvzV_IXg.html', 'http://g1.ykimg.com/051600005719C6A767BC3C0B7E08301B', '优酷|土豆', 0, 6665915, 'XXX', '2016-04-29', '', 93, 1),
('疯狂动物城', '电影', '美国', '动画|冒险', '', 'http://v.youku.com/v_show/id_XMTU3MjI1MTk1Mg==.html|http://www.tudou.com/albumplay/dNyv9o4aFto/ifobcSD81Hk.html', 'http://g2.ykimg.com/0516000056AEC3E767BC3C4574092CD3', '爱奇异|土豆', 0, 31985502, 'XXX', '2016-01-29', '', 95, 1),
('海贼王', '电影', '美国', '冒险|动作', '', 'http://www.iqiyi.com/v_19rrhtpv5k.html', 'http://g3.ykimg.com/051600004FB2609F0000015BB40523B3', '爱奇异', 1, 15671, 'XXX', '2006-06-27', '', 62, 1),
('功夫熊猫3', '电影', '美国|大陆', '动画|冒险|动作', '', 'http://v.youku.com/v_show/id_XMTU2NTk5MDgxMg==.html|http://www.tudou.com/albumplay/bLS2BJbt2y0/BkBFW1mtTH8.html', 'http://g2.ykimg.com/051600005732A53C67BC3C1C5E01180E', '优酷|土豆', 0, 1201773380, 'XXX', '2015-7-10', '', 95, 1),
('西游记之三大白骨精', '电影', '大陆', '奇幻|动作', '', 'http://v.youku.com/v_show/id_XMTUyNjAyMzcxMg==.html|http://www.tudou.com/albumplay/JQUxeNt8fJw/2Ze--TmJSAk.html', 'http://g4.ykimg.com/0516000056B01AAE67BC3C2A660716C7', '优酷|土豆', 0, 34232370, 'XXX', '2016-02-08', '', 91, 1),
('星球大战7：原力觉醒', '电影', '美国', '科幻|动作|冒险', '', 'http://v.youku.com/v_show/id_XMTUzMjI2OTE0NA==.html|http://www.tudou.com/albumplay/IYZHp8ERwQg/ZKx1ax2YtN0.html', 'http://g2.ykimg.com/05160000570B4E9067BC3C7F360D80C1', '优酷|土豆', 0, 33558393, 'XXX', '2015-12-18', '', 92, 1),
('魁拔3：战神崛起', '电影', '大陆', '动画|动作|冒险', '', 'http://v.youku.com/v_show/id_XODQ3Mzc4Mjg0.html|http://www.tudou.com/albumplay/G6OxUZPgK4A/RhHFM3k-bMw.html', 'http://g1.ykimg.com/051600005476828667379F6BDF0A6AE9', '优酷|土豆', 0, 30988789, 'XXX', '2014-10-01', '', 92, 1),
('霍比特人3：五军之战', '电影', '美国|新西兰', '奇幻|冒险', '', 'http://v.youku.com/v_show/id_XOTMwMjQ2MDI4.html', 'http://g2.ykimg.com/0516000054B8C88367379F1DCE0DAC85', '优酷', 1, 12609750, 'XXX', '2014-12-04', '', 92, 1),
('火影忍者', '动漫', '日本', '番剧', '格斗|冒险', 'http://v.youku.com/v_show/id_XNTQwMTgxMTE2.html|http://www.tudou.com/albumplay/Lqfme5hSolM/QFEG6YaMBs8.html', 'http://g1.ykimg.com/051600005563E58467BC3C1E0C049028', '优酷|土豆', 0, 1735734029, 'XXX', '2002-10-03', '', 99, 685),
('秦时明月之君临天下', '动漫', '大陆', '番剧', '历史|冒险', 'http://v.youku.com/v_show/id_XODU2MTEyNjI4.html|http://www.tudou.com/albumplay/qJtXzLi3iaY/-LXrcdT3YCU.html', 'http://g3.ykimg.com/0516000051D280816758394C8A0163A9', '优酷|土豆', 0, 577069215, 'XXX', '2014-00-00', '', 99, 39),
('黑甲 第一季', '动漫', '大陆', '番剧', '搞笑|冒险', 'http://v.youku.com/v_show/id_XMTU0MjMxOTg4MA==.html|http://www.tudou.com/albumplay/F_2fKifcecU/lPOuvDR1vDo.html', 'http://g1.ykimg.com/05160000571ACE2E67BC3C697A08D44D', '优酷|土豆', 0, 8238466, 'XXX', '2016-00-00', '', 95, 6),
('镇魂街', '动漫', '大陆', '番剧', '冒险', 'http://v.youku.com/v_show/id_XMTU1MDcxNDIyOA==.html|http://www.tudou.com/albumplay/DCHMvTnGguE/I4woCOSIHMw.html', 'http://g3.ykimg.com/05160000572068AA67BC3C683D0BF888', '优酷|土豆', 0, 19700537, 'XXX', '2016-04-28', '', 97, 8),
('画江湖之灵主', '动漫', '大陆', '番剧', '冒险|历史', 'http://v.youku.com/v_show/id_XMTM0ODY4NzY1Mg==.html|http://www.tudou.com/albumplay/qrCSg27heOI/UPWTbqkH3L0.html|http://www.mgtv.com/v/7/158034/f/1793725.html|http://vod.kankan.com/v/89/89422/493769.shtml?id=731057|http://www.fun.tv/vplay/g-202818.v-648462/', 'http://g2.ykimg.com/0516000055E6C99767BC3C13D20D9E4B', '优酷|土豆|芒果TV|响巢|风行', 0, 105111968, 'XXX', '2015-10-08', '', 97, 37),
('百武装战记', '动漫', '日本', '番剧', '格斗|美少女', 'http://v.youku.com/v_show/id_XMTUyMTEzMzU0OA==.html|http://www.tudou.com/albumplay/_s4Rzz-KIEw/lEi9C0TaQFo.html|http://www.bilibili.com/video/av4278571', 'http://g4.ykimg.com/0516000056E2679E67BC3C6C8808B66E', '优酷|土豆|bilibili', 0, 11001688, 'XXX', '2016-04-04', '', 94, 12),
('天空之城', '动漫', '日本', '剧场', '恋爱|科幻', 'http://www.iqiyi.com/w_19rrdfm1p1.html', 'http://g3.ykimg.com/051600005434D8E667379F19E001B9C5', '爱奇异', 1, 7274030, 'XXX', '1986-08-02', '', 84, 1);


