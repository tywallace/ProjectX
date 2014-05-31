-- Table: "signs"

DROP TABLE "signs";

CREATE TABLE "signs"
(
ID varchar,
STARTIME varchar,
ENDTIME varchar,
AMPM varchar,
DAY varchar,
PRIMARY KEY (ID)
);

COPY "signs" FROM 'C:\Users\Tyler\Documents\RampUp\ProjectX\signs_final.csv' USING DELIMITERS ',' CSV;