USE webtoon;

DROP TABLE if EXISTS title_genre;

CREATE TABLE title_genre(
	titleID INT NOT NULL,
	titleName VARCHAR(255) NOT NULL,
	authorID INT NOT NULL,
    authorName VARCHAR(255) NOT NULL,
	genre VARCHAR(255) NOT NULL,
	`rank` INT NOT NULL,
    new_index INT NOT NULL  PRIMARY KEY
);

LOAD DATA LOCAL INFILE '/Users/andy/Desktop/github/DE_project/naver_webtoon/data/title_genre.csv'
INTO TABLE title_genre
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 ROWS
(new_index, `rank`, genre, titleName, titleID, authorName, authorID);

SELECT *
  FROM webtoon.title_genre;

