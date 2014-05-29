-- Table: "SIGNS"

-- DROP TABLE "SIGNS";

DROP TABLE "SIGNS";

CREATE TABLE "SIGNS"
(
ID varchar,
STARTIME varchar,
ENDTIME varchar,
AMPM varchar,
DAY varchar,
PRIMARY KEY (ID)
);

COPY "SIGNS" FROM 'C:\Users\Tyler\Documents\RampUp\ProjectX\signs_final.csv' USING DELIMITERS ',' CSV;