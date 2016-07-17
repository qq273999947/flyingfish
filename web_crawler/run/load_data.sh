

mysql -u${mysql_user} -p${mysql_passwd} -h${host} -e "
    use flyingfish;
    LOAD DATA LOCAL INFILE 'animelist_20160717.txt' into table video(
        name, classify_1, classify_2, classify_3, classify_4, link, picture_url, source, is_unique, count, intro, start_time, update_time, score, drama_num
    );
"
