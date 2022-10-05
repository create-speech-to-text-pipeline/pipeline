CREATE TABLE IF NOT EXISTS amharicnews
(
    "uid" TEXT NOT NULL,
    "headline" TEXT NOT NULL,
    "category" VARCHAR(20) DEFAULT NULL,
    "date" VARCHAR(30) DEFAULT NULL,
    "views" INT DEFAULT NULL,
    "article" TEXT DEFAULT NULL,
    "link" TEXT DEFAULT NULL,
    PRIMARY KEY ("uid")
);