drop database if exists `flyingfish`;
create database if not exists `flyingfish`;

drop table if exists `video`;
create table `video` (
	`id`			int unsigned 	not null 	auto_increment	comment '自增主键',
    `name`			varchar(50)		not null	default ''	comment '视频名称',
    `classify_1`	varchar(30)		not null	default ''	comment '一级分类',
    `classify_2`	varchar(30)		not null	default ''	comment '二级分类',
    `classify_3`	varchar(30)		not null	default ''	comment '三级分类',
    `classify_4`	varchar(30)		not null	default ''	comment '四级分类',
    `link`			varchar(50)		not null	default ''	comment '视频链接',
    `picture_url`	varchar(50)		not null	default ''	comment '缩略图地址',
    `source`		varchar(200)	not null	default ''	comment '视频源',
    `is_unique`		smallint		not null	default 0	comment '是否独播',
    `count`			int				not null	default 0	comment '播放量',
    `intro`			varchar(500)	not null	default ''	comment '简介',
    `start_time`	datetime		not null	default '1970-01-01 00:00:00'	comment '上映时间',
    `update_time`	datetime		not null	default '1970-01-01 00:00:00'	comment '更新时间',
    `score`			smallint		not null	default 0	comment '评分',
    `drama_num`		smallint		not null	default 1	comment	'剧集数',
    primary key (`id`),
    unique  key (`link`, `source`)
) comment '视频信息表' default charset=utf8mb4;
