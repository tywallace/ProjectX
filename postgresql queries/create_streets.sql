-- Table: "streets"

DROP TABLE "streets";

CREATE TABLE "streets"
(
ID varchar,
BORO varchar,
STREET varchar,
CROSS1 varchar,
CROSS2 varchar,
SIDE varchar,
Primary Key(ID)
);

COPY "streets" FROM 'C:\Users\Tyler\Documents\RampUp\ProjectX\street_final_sql.csv' USING DELIMITERS ',' CSV;