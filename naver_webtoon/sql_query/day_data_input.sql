LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/platform_included_data/webtoon_mon_data.csv'
INTO TABLE mon_webtoon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(`rank`, day, titleName, titleID, authorName, authorID, rating, url, platform);

LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/platform_included_data/webtoon_tue_data.csv'
INTO TABLE tue_webtoon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(`rank`, day, titleName, titleID, authorName, authorID, rating, url, platform);

LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/platform_included_data/webtoon_wed_data.csv'
INTO TABLE wed_webtoon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(`rank`, day, titleName, titleID, authorName, authorID, rating, url, platform);

LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/platform_included_data/webtoon_thu_data.csv'
INTO TABLE thu_webtoon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(`rank`, day, titleName, titleID, authorName, authorID, rating, url, platform);

LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/platform_included_data/webtoon_fri_data.csv'
INTO TABLE fri_webtoon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(`rank`, day, titleName, titleID, authorName, authorID, rating, url, platform);

LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/platform_included_data/webtoon_sat_data.csv'
INTO TABLE sat_webtoon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(`rank`, day, titleName, titleID, authorName, authorID, rating, url, platform);

LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/platform_included_data/webtoon_sun_data.csv'
INTO TABLE sun_webtoon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(`rank`, day, titleName, titleID, authorName, authorID, rating, url, platform);

LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/platform_included_data/webtoon_dailyPlus_data.csv'
INTO TABLE daily_webtoon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(`rank`, day, titleName, titleID, authorName, authorID, rating, url, platform);

LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/platform_included_data/webtoon_new_data.csv'
INTO TABLE new_webtoon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(`rank`, day, titleName, titleID, authorName, authorID, rating, url, platform);

LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/platform_included_data/webtoon_finish_data.csv'
INTO TABLE finish_webtoon
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(`rank`, day, titleName, titleID, authorName, authorID, rating, url, platform);

